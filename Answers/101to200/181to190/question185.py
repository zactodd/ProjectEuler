"""
Question 185:
The game Number Mind is a variant of the well known game Master Mind.

Instead of coloured pegs, you have to guess a secret sequence of digits. After each guess you're only told in how many places you've guessed the correct digit. So, if the sequence was 1234 and you guessed 2036, you'd be told that you have one correct digit; however, you would NOT be told that you also have another digit in the wrong place.

For instance, given the following guesses for a 5-digit secret sequence,

90342 ;2 correct
70794 ;0 correct
39458 ;2 correct
34109 ;1 correct
51545 ;2 correct
12531 ;1 correct

The correct sequence 39542 is unique.

Based on the following guesses,

5616185650518293 ;2 correct
3847439647293047 ;1 correct
5855462940810587 ;3 correct
9742855507068353 ;3 correct
4296849643607543 ;3 correct
3174248439465858 ;1 correct
4513559094146117 ;2 correct
7890971548908067 ;3 correct
8157356344118483 ;1 correct
2615250744386899 ;2 correct
8690095851526254 ;3 correct
6375711915077050 ;1 correct
6913859173121360 ;1 correct
6442889055042768 ;2 correct
2321386104303845 ;0 correct
2326509471271448 ;2 correct
5251583379644322 ;2 correct
1748270476758276 ;3 correct
4895722652190306 ;1 correct
3041631117224635 ;3 correct
1841236454324589 ;3 correct
2659862637316867 ;2 correct

Find the unique 16-digit secret sequence.
"""
import random

GENERATION_SIZE = 32
FITTEST = 16
MUTATION_RATE = 5
SEED = random.SystemRandom()
GUESSES = {
    "5616185650518293": 2,
    "3847439647293047": 1,
    "5855462940810587": 3,
    "9742855507068353": 3,
    "4296849643607543": 3,
    "3174248439465858": 1,
    "4513559094146117": 2,
    "7890971548908067": 3,
    "8157356344118483": 1,
    "2615250744386899": 2,
    "8690095851526254": 3,
    "6375711915077050": 1,
    "6913859173121360": 1,
    "6442889055042768": 2,
    "2321386104303845": 0,
    "2326509471271448": 2,
    "5251583379644322": 2,
    "1748270476758276": 3,
    "4895722652190306": 1,
    "3041631117224635": 3,
    "1841236454324589": 3,
    "2659862637316867": 2
}


good_seeds = set()


def setup_answers(answers):
    for j in range(0, max(len(good_seeds), 8)):
        s = ""
        for i in range(0, 16):
            x = SEED.randint(0, 9)
            s += str(x)
        answers.append(s)
    for s in good_seeds:
        answers.append(s)


def score(answers):
    scores = []
    for a in answers:
        s = 0
        for guess in GUESSES:
            matches = 0
            guess = GUESSES[guess]
            for i in range(0, len(guess)):
                if a[i] == guess[i]:
                    matches += 1
            if matches == guess:
                s += 1
        scores.append(s)
    return scores


def fittest(answers, scores):
    best_answers = [""] * FITTEST
    best_scores = [0] * FITTEST
    worst_best_score = 0
    for i, s in enumerate(scores):
        if s > worst_best_score:
            update_worst = 99
            for j in range(0, len(best_scores)):
                if best_scores[j] == worst_best_score:
                    best_scores[j] = s
                    best_answers[j] = answers[i]
                if best_scores[j] < update_worst:
                    update_worst = best_scores[j]
            worst_best_score = update_worst
    return best_answers, best_scores


def next_gen(best_answers):
    answers = []
    for i in range(0, GENERATION_SIZE):
        s = ""
        for i in range(0, 16):
            m = SEED.randint(0, MUTATION_RATE)
            if m == 0:
                s += str(SEED.randint(0, 9))
            else:
                x = SEED.randint(0, len(best_answers) - 1)
                s += best_answers[x][i]
        assert (len(s) == 16)
        answers.append(s)
    return answers


def is_inbread(answers):
    s = answers[0]
    return all(a == s for a in answers)


def answer():
    best_score = 0
    answers = []
    setup_answers(answers)
    while best_score < len(GUESSES):
        scores = score(answers)
        best_answers, best_scores = fittest(answers, scores)
        if best_score < best_scores[0]:
            best_score = best_scores[0]
            if best_score < 20:
                good_seeds.clear()
            print(best_score, best_answers)
        if best_score == best_scores[0]:
            x = len(good_seeds)
            good_seeds.add(best_answers[0])
            if not len(good_seeds) == x:
                print(len(good_seeds))
        answers = next_gen(best_answers)
        if is_inbread(answers):
            answers = []
            setup_answers(answers)
    return


if __name__ == '__main__':
    print("Answer is:", answer())

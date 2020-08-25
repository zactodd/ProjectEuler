"""
Problem 191:

A particular school offers cash rewards to children with good attendance and punctuality. If they are absent for three consecutive days or late on more than one occasion then they forfeit their prize.

During an n-day period a trinary string is formed for each child consisting of L's (late), O's (on time), and A's (absent).

Although there are eighty-one trinary strings for a 4-day period that can be formed, exactly forty-three strings would lead to a prize:

OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
LAOO LAOA LAAO

How many "prize" strings exist over a 30-day period?
"""


def nested_lists(value, *dims):
    return [value] * dims[0] if len(dims) == 1 else [nested_lists(value, *dims[1:]) for _ in range(dims[0])]


def answer(days=30, absents=2, lates=1):
    ps = nested_lists(0, days + 1, absents + 1, lates + 1)
    ps[0][0][0] = 1
    for i in range(1, len(ps)):
        ps[i][0][0] = sum(ps[i - 1][j][0] for j in range(absents + 1))
        ps[i][0][1:len(ps[i][0])] = [sum(sum(ps[i - 1][j][k - 1:k + 1]) for j in range(absents + 1))
                                     for k in range(1, len(ps[i][0]))]
        ps[i][1:len(ps[i])] = [[ps[i - 1][j - 1][k] for k in range(len(ps[i][j]))] for j in range(1, len(ps[i]))]
    return sum(map(sum, ps[days]))


if __name__ == "__main__":
    print("Answer is:", answer())

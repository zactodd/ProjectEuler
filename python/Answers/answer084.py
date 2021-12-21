"""
Problem 84:
In the game, Monopoly, the standard board is set up in the following way:

GO	A1	CC1	A2	T1	R1	B1	CH1	B2	B3	JAIL
H2	 	C1
T2	 	U1
H1	 	C2
CH3	 	C3
R4	 	R2
G3	 	D1
CC3	 	CC2
G2	 	D2
G1	 	D3
G2J	F3	U2	F2	F1	R3	E3	E2	CH2	E1	FP
A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
Advance to GO
Go to JAIL
Chance (10/16 cards):
Advance to GO
Go to JAIL
Go to C1
Go to E3
Go to H2
Go to R1
Go to next R (railway company)
Go to next R
Go to next U (utility company)
Go back 3 squares.
The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for which the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to another square, and it is the final square that the player finishes at on each roll that we are interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to produce strings that correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.
"""

import random


class Deck(object):
    def __init__(self, size):
        self.deck = list(range(size))
        self.stack = []

    def next_card(self):
        if not len(self.stack):
            self.stack = self.deck.copy()
            random.shuffle(self.stack)
        return self.stack.pop()


def update_location(location, chance, community_chest):
    match location:
        case 7 | 22 | 36:  # Chance
            match chance.next_card():
                case 0:
                    return 0
                case 1:
                    return 10  # Go to jail just visiting
                case 2:
                    return 11
                case 3:
                    return 24
                case 4:
                    return 39
                case 5:
                    return 5
                case 6 | 7:  # Next railway
                    return (location + 5) // 10 % 4 * 10 + 5
                case 8:  # Next utility
                    return 28 if (12 < location < 28) else 12
                case 9:
                    location = location - 3
                    return update_location(location, chance, community_chest)
        case 30:  # Go to jail
            return 10
        case 2 | 17 | 33:  # Community chest
            match community_chest.next_card():
                case 0:
                    return 0  # Go to go
                case 1:
                    return 10  # Go to jail just visiting
    return location


def answer(samples=10 ** 7):
    counts = [0] * 40
    chance = Deck(16)
    community_chest = Deck(16)
    triple_doubles = 0
    location = 0

    for _ in range(samples):
        d0, d1 = random.randint(1, 4), random.randint(1, 4)
        triple_doubles += d0 == d1
        if triple_doubles >= 3:
            location = 30
            triple_doubles = 0
        else:
            location = (location + d0 + d1) % 40
        location = update_location(location, chance, community_chest)
        counts[location] += 1

    return "".join("{:02d}".format(i) for (i, c) in sorted(enumerate(counts), key=(lambda ic: -ic[1]))[: 3])


if __name__ == '__main__':
    print("Answer is:", answer())

'''
--- Part Two ---
To make things a little more interesting, the Elf introduces one additional rule. Now, J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.

To balance this, J cards are now the weakest individual cards, weaker even than 2. The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

J cards can pretend to be whatever card is best for the purpose of determining hand type; for example, QJJQ2 is now considered four of a kind. However, for the purpose of breaking ties between two hands of the same type, J is always treated as J, not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.

Now, the above example goes very differently:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
KK677 is now the only two pair, making it the second-weakest hand.
T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.
With the new joker rule, the total winnings in this example are 5905.

Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?
'''

import re

SORT_ORDER = 'AKQT98765432J'

file = open('Input', 'r')

lines = file.readlines()

fiveOAKRegex = r'(.)(\1){4}'
fourOAKRegex = r'(.)(\1){3}'
fullHouseRegex = r'(.)(\1){2}(.)\3'
altFullHouseRegex = r'(.)(\1)(.)\3{2}'
threeOAKRegex = r'(.)(\1){2}'
pairRegex = r'(.)\1'

possibleJokerComboes ={
    (1, 1): 0,
    (1, 4): 0,
    (2, 2): 0,
    (2, 3): 0,
    (3, 1): 1,
    (3, 3): 1,
    (4, 1): 2,
    (4, 2): 1,
    (5, 1): 3,
    (5, 2): 3,
    (6, 1): 5
}

processedHands = []


def check_jokers(hand):
    return sum(1 for _ in re.finditer(r'J', hand))


def check_type(regex, hand, is_two_pair=False):
    number_of_matches = 1
    if is_two_pair:
        number_of_matches = 2
    return sum(1 for _ in re.finditer(regex, hand)) == number_of_matches


def hand_encoding(hand):
    return (SORT_ORDER.index(card) for card in hand)


def process_hand(hand, num_of_jokers, curr_type):
    encoded_hand = hand_encoding(hand)
    if (curr_type, num_of_jokers) in possibleJokerComboes:
        processedHands.append((possibleJokerComboes[(curr_type, num_of_jokers)], *encoded_hand, bet))
    else:
        processedHands.append((curr_type, *encoded_hand, bet))


for line in lines:
    hand = line.split(' ')[0]
    bet = int(line.split(' ')[1].strip())
    sortedHand = ''.join(sorted(hand))

    if check_type(fiveOAKRegex, sortedHand):
        process_hand(hand, check_jokers(hand), 0)

    elif check_type(fourOAKRegex, sortedHand):
        process_hand(hand, check_jokers(hand), 1)

    elif check_type(fullHouseRegex, sortedHand) or check_type(altFullHouseRegex, sortedHand):
        process_hand(hand, check_jokers(hand), 2)

    elif check_type(threeOAKRegex, sortedHand):
        process_hand(hand, check_jokers(hand), 3)

    elif check_type(pairRegex, sortedHand, True):
        process_hand(hand, check_jokers(hand), 4)

    elif check_type(pairRegex, sortedHand) == 1:
        process_hand(hand, check_jokers(hand), 5)

    else:
        process_hand(hand, check_jokers(hand), 6)

currRank = 1

processedHands.sort(reverse=True)
total = 0

for hand in processedHands:
    total += hand[6] * currRank
    currRank += 1

print(total)

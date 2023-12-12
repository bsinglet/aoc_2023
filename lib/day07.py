#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '11 December 2023'
__version__ = '0.1.0'


def get_input_data(filename: str) -> list:
    with open(filename, 'r') as my_file:
        puzzle_input = my_file.read()
    puzzle_input = [x.strip() for x in puzzle_input.strip().split('\n')]
    return puzzle_input


type_rank = {
    'Five of a kind': 7,
    'Four of a kind': 6,
    'Full house': 5,
    'Three of a kind': 4,
    'Two pair': 3,
    'One pair': 2,
    'High card': 1,
}

card_rank = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}


def get_hand_type(hand: str) -> str:
    value = None
    unique_characters = list(set([x for x in hand]))
    sorted_hand = [x for x in hand]
    sorted_hand.sort()
    sorted_hand = ''.join(sorted_hand)
    if len(hand) != 5:
        return None
    if len(unique_characters) == 1:
        value = 'Five of a kind'
    elif len(unique_characters) == 2 and (unique_characters[0] * 4 in sorted_hand or unique_characters[1] * 4 in sorted_hand):
        value = 'Four of a kind'
    elif len(unique_characters) == 2 and (unique_characters[0] * 3 in sorted_hand or unique_characters[1] * 3 in sorted_hand):
        value = 'Full house'
    elif len(unique_characters) == 3 and (unique_characters[0] * 3 in sorted_hand or unique_characters[1] * 3 in sorted_hand or unique_characters[2] * 3 in sorted_hand):
        value = 'Three of a kind'
    elif len(unique_characters) == 3 and ((sorted_hand[0] == sorted_hand[1] and sorted_hand[2] == sorted_hand[3]) or (sorted_hand[0] == sorted_hand[1] and sorted_hand[3] == sorted_hand[4]) or (sorted_hand[1] == sorted_hand[2] and sorted_hand[3] == sorted_hand[4])):
        value = 'Two pair'
    elif len(unique_characters) == 4:
        value = 'One pair'
    else:
        value = 'High card'
    return value


def hand_greater_than_or_equal(hand1, hand2):
    hand1_type = get_hand_type(hand1)
    hand2_type = get_hand_type(hand2)
    if hand1_type != hand2_type:
        return type_rank[hand1_type] >= type_rank[hand2_type]
    for index in range(len(hand1)):
        card1_rank = card_rank[hand1[index]]
        card2_rank = card_rank[hand2[index]]
        if card1_rank != card2_rank:
            return card1_rank >= card2_rank
    return True


def parse_hands(puzzle_input: list) -> list:
    result = list()
    for each_line in puzzle_input:
        each_line = each_line.split(' ')
        result.append((each_line[0].strip(), each_line[1].strip()))
    return result


def sort_hands(hands_bids: list) -> list:
    for index in range(len(hands_bids)-1):
        for index2 in range(index, len(hands_bids)):
            if not hand_greater_than_or_equal(hands_bids[index][0], hands_bids[index2][0]):
                temp = hands_bids[index]
                hands_bids[index] = hands_bids[index2]
                hands_bids[index2] = temp
    return hands_bids


def score_hands(hands_bids: list) -> int:
    score = 0
    for index in range(len(hands_bids)):
        # print(f"{score} += {len(hands_bids) - index} * {int(hands_bids[index][1])}")
        score += (len(hands_bids) - index) * int(hands_bids[index][1])
    return score


def day_07_part_1(puzzle_input: list) -> int:
    hands_bids = parse_hands(puzzle_input)
    hands_bids = sort_hands(hands_bids)
    return score_hands(hands_bids)


def main() -> None:
    puzzle_input = get_input_data("inputs/input_07.txt")
    part_1 = day_07_part_1(puzzle_input=puzzle_input)
    print(f"The total winnings for part 1 are {part_1}.")


if __name__ == '__main__':
    main()

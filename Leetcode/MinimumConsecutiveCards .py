
def minimumCardPickup(self, cards: List[int]) -> int:
    freq = {}
    min_len = 10000000
    # for card in cards:;
    #     if card in freq:
    #         freq[card] += 1
    #     else:
    #         freq[card] = 1

    for i in range(len(cards)):
        x = cards[i]
        if x in freq:
            min_len = min(min_len, (i + 1 - freq[cards[i]]))
            freq[x] = i
        else:
            freq[x] = i
    if min_len == 10000000:
        min_len = -1
    return min_len

# You are given an integer array cards where cards[i] represents the value of the ith card.
# A pair of cards are matching if the cards have the same value.
#
# Return the minimum number of consecutive cards you have to pick up to have a pair of matching
# cards among the picked cards. If it is impossible to have matching cards, return -1.
#
# Example 1:
#
# Input: cards = [3,4,2,3,4,7]
# Output: 4
# Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3.
# Note that picking up the cards [4,2,3,4] is also optimal.
# Example 2:
#
# Input: cards = [1,0,5,3]
# Output: -1
# Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.
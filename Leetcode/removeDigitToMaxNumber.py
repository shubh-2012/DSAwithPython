
def removeDigit(self, number: str, digit: str) -> str:
    ex = ''
    pos = []
    for i in range(0 ,len(number)):
        if number[i] != digit:
            ex = ex + number[i]
        else:
            if i == len(number) - 1:
                pos.append(int(number[:i]))
            else:
                pos.append(int(ex + number[ i +1:]))
                ex = ex + number[i]

    return str(max(pos))

# Return the resulting string after removing exactly one occurrence of digit from number such
# that the value of the
# resulting string in decimal form is maximized.
# The test cases are generated such that digit occurs at least once in number.
#
# Example 1:
#
# Input: number = "123", digit = "3"
# Output: "12"
# Explanation: There is only one '3' in "123". After removing '3', the result is "12".
# Example 2:
#
# Input: number = "1231", digit = "1"
# Output: "231"
# Explanation: We can remove the first '1' to get "231" or remove the second '1' to get "123".
# Since 231 > 123, we return "231".
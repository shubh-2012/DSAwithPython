

def plusone(digits):
    i = len(digits)-1
    if digits[i] < 9:
        digits[i] += 1
    else:
        while digits[i] == 9 and i > 0:
            digits[i] = 0
            i -= 1
        if digits[i] == 9:
            digits[i] = 0
            digits.insert(0, 1)
        else:
            digits[i] += 1


inp = [1,2,3]

plusone(inp)

print(inp, "\n")
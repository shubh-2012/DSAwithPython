# The isBadVersion API is already defined.
# def isBadVersion(version: int) -> bool:

def binSearch(self, l, r):
    # if r - l == 0:
    #     return False
    mid = (l + r) // 2

    if isBadVersion(mid) == False:
        if isBadVersion(mid + 1) == True:
            return mid + 1
        else:
            return binSearch(self, mid + 1, r)

    else:
        if isBadVersion(mid - 1) == False:
            return mid
        else:
            return binSearch(self, l, mid - 1)


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n

        x = (binSearch(self, l, r))

        return x

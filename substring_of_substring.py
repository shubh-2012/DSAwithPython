

# find substring of a string , whose substring is not prefix or suffix of the original string

string =  input()

last,ans = 0,0
for i in range(len(string)):
    if (string[i] == string[0] or string[i] == string[-1]):
        last = i
        continue
    ans = max(ans, i - last)
if(ans == 0): print(-1)
else: print(ans)



test = {}
test["test1"] ={}
test["test2"] = {}

test["test1"]["score1"] = 20
test["test1"]["score2"] = 30
test["test2"]["score1"] = 30

print(test)

for k in test.keys():
    print(k)

for k in test.values():
    print(k)


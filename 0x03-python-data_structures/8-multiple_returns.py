#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])

result1 = multiple_returns("welcome, at Holberton")
print(result1)

result2 = multiple_returns("")
print(result2)


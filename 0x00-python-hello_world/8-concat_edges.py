#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
del str[:33]; str.remove("o"); str.remove(" "); str.remove("w"); str.remove("i")
print(str[:30] + str[65:72] + str[0] + str[30:38] + str[-11:-3])

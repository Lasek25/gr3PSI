def reverse(word):
    #return word[len(word)::-1]
    return word[::-1]


a = "pieseł i koteł"
print(a + " -> " + reverse(a))
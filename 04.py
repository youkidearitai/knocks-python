string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

words = string.split(" ")
elements = {}

onestrings = [1, 5, 6, 7, 8, 9, 15, 16, 19]

for i in range(len(words)):
    if i in onestrings:
        elements[words[i][0:1]] = i
    else:
        elements[words[i][0:2]] = i

print(elements)

elements = {
    words[i][0: 1 if i in onestrings else 2]: i + 1 for i in range(len(words))
}
print(elements)



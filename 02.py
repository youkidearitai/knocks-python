string1 = 'パトカー'
string2 = 'タクシー'

def merge_string(string1, string2):
    ret = []
    for i in range(len(string1)):
        ret.append(string1[i])
        ret.append(string2[i])

    return "".join(ret)

def zip_merge(string1, string2):
    ret = ''
    for (a, b) in zip(string1, string2):
        ret += a + b
    return ret

print(merge_string(string1, string2))
print(zip_merge(string1, string2))

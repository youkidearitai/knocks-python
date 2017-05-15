string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
splited = string.rsplit(" ")
names = [len(i.rstrip(",.")) for i in splited]

print(names)

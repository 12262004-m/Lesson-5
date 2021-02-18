new = open("lesson 5.3 file with str", "r", encoding="utf-8")
k = new.read().split("\n")
count = 0
for i in k:
    i = i.split()
    if float(i[1]) < 20000.0:
        count+=1
print(count)
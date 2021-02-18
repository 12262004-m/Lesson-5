new = open("lesson 5.2 file with str", "r", encoding="utf-8")
count = 0
for i in new:
    count+=1
print("Количество строк в файле: ", count, end = " ")
print()
new = open("lesson 5.2 file with str", "r", encoding="utf-8")
new2 = new.readlines()
count = 1
for j in range(len(new2)):
    print("Количество слов в строке", count,  "равно", len(new2[j].split()))
    count+=1

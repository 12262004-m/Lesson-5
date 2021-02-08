from translate import Translator

new = open("text_4.txt", "r", encoding="utf-8")
k = new.readlines()
for i in k:
    print(i, end="")

new = open("text_4.txt", "r", encoding="utf-8")
k = new.read().split("\n")
print()
for i in k:
    i = i.split()
    print(Translator(from_lang="Russian", to_lang="English").translate(i[0]))

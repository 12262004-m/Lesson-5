new = open("lesson 5.1 add", "w", encoding="utf-8")
i = input("add:  ")
while i != "":
    new.write(f"{i}\n")
    i = input("add :  ")
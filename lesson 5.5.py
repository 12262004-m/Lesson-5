with open("lesson 5.5 file", "w", encoding="utf-8") as new:
    k = input("Введите числа для добавления в файл: ")
    new.writelines(k)
    number = k.split()
    print(sum(map(int, number)))

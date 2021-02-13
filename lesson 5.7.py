
import json

summa = 0
with open("lesson 5.7 js.json", "w", encoding="utf-8") as new1:
    with open("lesson 5.7 file", encoding="utf-8") as new2:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in new2}
        for i in profit.values():
            if int(i) > 0:
                summa += int(i)
    k = len([int(i) for i in profit.values() if int(i) > 0])
    result = [profit, summa / k]

json.dump(result, new1, ensure_ascii=False, indent=4)

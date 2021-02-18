new_dict = {}
numbers = "1234567890 "
with open("lesson 5.6 file", "r", encoding="utf-8") as new:
    for i in new:
        lesson, number = i.split(":")
        new_dict[lesson] = sum(map(int, "".join([k for k in number if k in numbers]).split()))
print(new_dict)
import sys

input_txt = open(sys.argv[1], "r", encoding="UTF-8").read().splitlines()
input_names = sys.argv[2].split(",")
d = {}

for i in input_txt:
    student, university = i.split(":")
    d[student] = university[0:]

for name in input_names:
    try:
        print("Name:", name, "University:", d[name])
    except:
        print("No record of '{}' was found!".format(name))
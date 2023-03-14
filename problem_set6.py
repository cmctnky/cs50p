# 1. Lines

import sys

def cmd_check():
    if len(sys.argv) < 2:
        sys.exit("Too few cmd line args")
    if len(sys.argv) > 2:
        sys.exit("Too many cmd line args")
    if ".py" not in sys.argv[1]:
        sys.exit("Not python file")



def is_valid(par):
    if par.isspace():
        return True
    if par.lstrip().startswith("#"):
        return True
    return False


cmd_check()
try:
    file = open(sys.argv[1], "r")
    lines = file.readlines()
except FileNotFoundError:
    sys.exit("File not exist")

cnt = 0
for line in lines:
    if not is_valid(line):
        cnt += 1
print(cnt)


# 2. Pizza

import tabulate, sys, csv 

def cmd_check():
    if len(sys.argv) < 2:
        sys.exit("Too few cmd line args")
    if len(sys.argv) > 2:
        sys.exit("Too many cmd line args")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not csv file")


cmd_check()
try:
    file = open(sys.argv[1], "r")
    reader = csv.DictReader(file)
    print(tabulate.tabulate(reader, headers="keys", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File not found")



# 3. Scourgify

import sys, csv


def cmd_check():
    if len(sys.argv) < 3:
        sys.exit("Too few cmd line args")
    if len(sys.argv) > 3:
        sys.exit("Too many cmd line args")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not csv file")

try:
    cmd_check()
    arr = []
    with open(sys.argv[1],"r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            split_name = row["name"].split(",")
            arr.append({"first":split_name[1].lstrip(), "last":split_name[0], "house":row["house"]})
except FileNotFoundError:
    sys.exit("Cant read ", sys.argv[1])

with open(sys.argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"], lineterminator='\n')
    writer.writerow({"first":"first", "last":"last", "house":"house"})
    for row in arr:
        writer.writerow({"first":row["first"], "last":row["last"], "house":row["house"]})













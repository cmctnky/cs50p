
# 1. numb3rs

import re, sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if re.search("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        numbers = ip.split(".")
        for number in numbers:
            if int(number) < 0 or int(number) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()


# 2. Watch on Youtube
# link = <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
# src split, / split, array -1 index
import re, sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        url = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s)
        if url:
            return "https://youtu.be/" + url.groups()[3]
        else:
            return False
    else:
        return False
if __name__ == "__main__":
    main()


# 3. Working 9 to 5
import re, sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    hours_ = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if hours_:
        return True
if __name__ == "__main__":
    main()

# 4. Regular, um, Expressions



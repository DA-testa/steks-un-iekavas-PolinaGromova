# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i))

        if next in ")]}":
            if not opening_brackets_stack:
                return i+1
            a = opening_brackets_stack.pop()
            if not are_matching:
                return i+1

    if opening_brackets_stack:
        a = opening_brackets_stack.pop()
        return a.position + 1
    return "Success"

def main():
    print("F/I")
    do=input()
    if do=="F":
        name = input("Enter file name: ") 
        with open(name, "r", encoding="latin1") as file:
            text=file.read()
        mismatch = find_mismatch(text)
        if mismatch == "Success":
            print("Success")
        else:
            print(mismatch)
    elif do=="I":
        text = input()
        mismatch = find_mismatch(text)
        if mismatch == "Success":
            print("Success")
        else:
            print(mismatch)
    else: print("Input error")


if __name__ == "__main__":
    main()

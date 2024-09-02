#!/usr/bin/python3
for firstNum in range(9):
        for secondNum in range(1, 10):
            if secondNum > firstNum:
                print(f"{firstNum}{secondNum}", end="")
                if not (firstNum == 8 and secondNum == 9):
                    print(", ", end="")
print()

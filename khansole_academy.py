"""
File: khansole_academy.py
The program should generate simple addition problems 
that involve adding two 2-digit integers. The user 
should be asked for an answer to each problem. The 
program should determine if the answer was correct 
or not, and give the user an appropriate message. The
program should keep giving the user problems until the 
user has gotten 3 problems correct in a row.
"""

import random

CORRECT_ANSWERS_IN_ROW = 3

def main():

    correct_answers = 0
    while correct_answers != CORRECT_ANSWERS_IN_ROW:
        a = random.randint(10,99)
        b = random.randint(10,99)
        result = a + b
        print(f"What is {a} + {b}?")
        answer = int(input("Your answer: "))
        if answer == result:
            correct_answers += 1
            print("Correct! You've gotten " + str(correct_answers) + " correct in a row.")
        else:
            correct_answers = 0
            print("Incorrect. The expected answer is " + str(result))
    print("Congratulations! You mastered addition!")

if __name__ == '__main__':
    main()

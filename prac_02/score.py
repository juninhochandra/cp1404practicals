import random

PROMPT = "Enter score: "

def main():
    score = float(input(PROMPT))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input(PROMPT))
    print(get_result(score))
    # I don't quite get what the question is asking, maybe this?
    score = random.randint(0, 100)
    print(score)

def get_result(score):
    # returns a prompt message depending on the score.
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
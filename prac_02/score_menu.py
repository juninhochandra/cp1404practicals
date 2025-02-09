SCORE = "Enter score: "
MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

def main():
    # Get a valid score.
    score = float(input(SCORE))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input(SCORE))

    # Our menu.
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = float(input(SCORE))
            while score < 0 or score > 100:
                print("Invalid score")
                score = float(input(SCORE))
        elif choice == "P":
            print(get_result(score))
        elif choice == "S":
            print(get_stars(score))
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell.")

def get_result(score):
    # returns a prompt message depending on the score.
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def get_stars(score):
    # returns the number of stars depending on the score.
    return "*" * int(score)

main()
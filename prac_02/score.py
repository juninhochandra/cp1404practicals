"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

PROMPT = "Enter score: "

score = float(input(PROMPT))
while score < 0 or score > 100:
    print("Invalid score")
    score = float(input(PROMPT))

if  score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
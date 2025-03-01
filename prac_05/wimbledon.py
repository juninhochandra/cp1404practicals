"""
Wimbledon
Estimate: 30 minutes
Actual:   24 minutes
"""

FILE_NAME = "wimbledon.csv"

def main():
    champions_and_wins = dict()
    countries = set()

    wimbledon = get_file_contents()

    for champions in wimbledon:
        extract_information(champions, champions_and_wins, countries)

    print_information(champions_and_wins, countries)


def extract_information(champions, champions_and_wins, countries):
    champions = champions.split(",")
    country = champions[1]
    countries.add(country)
    champion = champions[2]
    if champion in champions_and_wins:
        champions_and_wins[champion] += 1
    else:
        champions_and_wins[champion] = 1


def get_file_contents():
    with open(FILE_NAME, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        return in_file.readlines()

def print_information(champions_and_wins, countries):
    print("Wimbledon Champions:")
    for champion, wins in champions_and_wins.items():
        print(f"{champion} {wins}")
    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

main()
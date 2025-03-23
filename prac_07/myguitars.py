import csv

from guitar import Guitar

def main():
    """Read file of guitar details, save as objects, display."""
    guitars = []
    read_guitars(guitars)
    add_guitars(guitars)

    guitars.sort()
    # Loop through and display all guitars (using their str method)
    for guitar in guitars:
        print(guitar)

def add_guitars(guitars):
    in_file = open('guitars.csv', 'a')
    guitar_name = input("Name: ")
    while guitar_name != "":
        """Input year and cost"""
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))

        """Create guitar object and append to guitars"""
        guitar = Guitar(guitar_name, guitar_year, guitar_cost)

        guitars.append(guitar)
        in_file.write(f"\n{guitar_name},{guitar_year},{guitar_cost}")
        print(f"{guitar_name:} ({guitar_year}) : ${guitar_cost} added.")
        print()
        guitar_name = input("Name: ")
    in_file.close()

def read_guitars(guitars):
    """Open the file for reading and store in a list"""
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    # Close the file as soon as we've finished reading it
    in_file.close()

main()
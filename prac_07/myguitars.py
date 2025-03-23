import csv

from guitar import Guitar

def main():
    """Read file of guitar details, save as objects, display."""
    guitars = []
    # Open the file for reading
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    # Close the file as soon as we've finished reading it
    in_file.close()

    # Loop through and display all guitars (using their str method)
    for guitar in guitars:
        print(guitar)

main()
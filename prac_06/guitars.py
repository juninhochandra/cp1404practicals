""" 21:49
Guitar
Estimate: 15 minutes
Actual:   35 minutes
"""

from prac_06.guitar import Guitar

print("My guitars!")

guitars = []
max_name_align = 0
max_cost_align = 0

guitar_name = input("Name: ")
while guitar_name != "":
    """Input year and cost"""
    guitar_year = int(input("Year: "))
    guitar_cost = float(input("Cost: &"))

    """Assign max alignment for printing"""
    max_name_align = max(max_name_align, len(guitar_name))
    max_cost_align = max(max_cost_align, len(f"{guitar_cost:0,.2f}"))

    """Create guitar object and append to guitars"""
    guitar = Guitar(guitar_name, guitar_year, guitar_cost)
    guitars.append(guitar)
    print(f"{guitar_name:} ({guitar_year}) : ${guitar_cost} added.")

    print()
    guitar_name = input("Name: ")

print("These are my guitars:")

for i, guitar in enumerate(guitars, start=1):
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>{max_name_align}} ({guitar.year}), worth $ {guitar.cost:>{max_cost_align},.2f}{vintage_string}")
"""
Guitar Test
Estimate: 5 minutes
Actual:   7 minutes
"""

from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 69420.50)

print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age()}")
print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age()}")
print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")
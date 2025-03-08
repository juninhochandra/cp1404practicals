""" 21.32
Guitar
Estimate: 10 minutes
Actual:   5 minutes
"""

from datetime import datetime

class Guitar:
    def __init__(self, name = "", year = 0, cost = 0):
        """Constructor"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Get the age of the guitar"""
        return datetime.now().year - self.year

    def is_vintage(self):
        return self.get_age() >= 50
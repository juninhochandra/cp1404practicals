"""
Programming Language
Estimate: 7 minutes
Actual:   7 minutes
"""

class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Constructor"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Returns true if the language is dynamically typed"""
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
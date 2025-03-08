"""
Languages
Estimate: 7 minutes
Actual:   7 minutes
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

programming_langs = [python, ruby, visual_basic]

print("The dynamically typed languages are:")
for programming_lang in programming_langs:
    if programming_lang.is_dynamic():
        print(programming_lang.name)
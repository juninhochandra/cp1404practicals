""" 19:56
Project
Estimate: 90 minutes
Actual:    minutes
"""

import datetime
from project import Project

FILE_NAME = "projects.txt"
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""

def main():
    print("Welcome to Pythonic Project Management")
    projects = []
    # Get projects from file
    load_projects(projects)
    print(f"Loaded {len(projects)} projects from {FILE_NAME}")

    # Menu interface
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            pass
        elif choice == "s":
            pass
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            pass
        elif choice == "a":
            pass
        elif choice == "u":
            pass
        else:
            pass
        print(MENU)
        choice = input(">>> ").lower()

def load_projects(projects):
    """Loaded projects from file and store in a list"""
    in_file = open(FILE_NAME, "r")
    in_file.readline()
    for line in in_file:
        parts = line.split("\t")
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)

def display_projects(projects):
    """Display the project in a formatted string"""
    print("Incomplete projects:")
    projects.sort()
    completed_projects = []
    for project in projects:
        if project.completion < 100:
            print(f"\t{project}")
        else:
            completed_projects.append(project)
    print("Completed projects:")
    for project in completed_projects:
        print(f"\t{project}")

main()
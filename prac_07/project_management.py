""" 19:56
Project
Estimate: 120 minutes
Actual:    minutes
"""

import datetime
from project import Project

FILE_NAME = "projects.txt"
PROJECT_CHOICE = "Project choice: "
PERCENTAGE_CHOICE = "New percentage: "
PRIORITY_CHOICE = "New priority: "
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""

def main():
    print("Welcome to Pythonic Project Management")

    # Get projects from file
    projects = load_projects()
    print(f"Loaded {len(projects)} projects from {FILE_NAME}")

    # Menu interface
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            projects = load_projects()
            print(f"Loaded {len(projects)} projects from {FILE_NAME}")
        elif choice == "s":
            pass
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            pass
        elif choice == "a":
            pass
        elif choice == "u":
            update_project(projects)
        else:
            pass
        print(MENU)
        choice = input(">>> ").lower()

def load_projects():
    """Loaded projects from file and store in a list"""
    projects = []
    in_file = open(FILE_NAME, "r")
    in_file.readline()
    for line in in_file:
        parts = line.split("\t")
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)
    return projects

def display_projects(projects):
    """Display the project in a formatted string"""
    print("Incomplete projects:")
    duplicate_projects = [project for project in projects]
    duplicate_projects.sort()
    completed_projects = []

    for project in duplicate_projects:
        if project.completion < 100:
            print(f"\t{project}")
        else:
            completed_projects.append(project)
    print("Completed projects:")
    for project in completed_projects:
        print(f"\t{project}")

def update_project(projects):
    """Update the project's percentage and priority"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_choice = input(PROJECT_CHOICE)
    is_valid_choice = False
    while not is_valid_choice:
        try:
            project_choice = int(project_choice)
            if project_choice > -1 or project_choice < len(projects):
                is_valid_choice = True
        except ValueError:
            project_choice = input(PROJECT_CHOICE)

    project = projects[project_choice]
    print(project)

    is_valid_choice = False
    percentage_choice = input(PERCENTAGE_CHOICE)
    if percentage_choice == "":
        is_valid_choice = True
    while not is_valid_choice:
        try:
            percentage_choice = int(percentage_choice)
            if percentage_choice > -1 or percentage_choice < 101:
                is_valid_choice = True
        except ValueError:
            percentage_choice = input(PERCENTAGE_CHOICE)

    is_valid_choice = False
    priority_choice = input(PRIORITY_CHOICE)
    if priority_choice == "":
        is_valid_choice = True
    while not is_valid_choice:
        try:
            priority_choice = int(priority_choice)
            if priority_choice > 0:
                is_valid_choice = True
        except ValueError:
            priority_choice = input(PRIORITY_CHOICE)

    if percentage_choice != "":
        setattr(project, "completion", percentage_choice)
    if priority_choice != "":
        setattr(project, "priority", priority_choice)

main()
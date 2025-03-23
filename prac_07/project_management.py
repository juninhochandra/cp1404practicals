""" 19:56
Project
Estimate: 120 minutes
Actual: 240 minutes
"""

import datetime
from operator import itemgetter
from project import Project

FILE_NAME = "projects.txt"
PROJECT_CHOICE = "Project choice: "
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
    projects = load_projects(FILE_NAME)
    print(f"Loaded {len(projects)} projects from {FILE_NAME}")

    # Menu interface
    is_saved = True
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            file_name = input("File: ")
            while file_name == "":
                file_name = input("File: ")
            projects = load_projects(file_name)
            print(f"Loaded {len(projects)} projects from {file_name}")
            is_saved = True
        elif choice == "s":
            save_projects(projects)
            is_saved = True
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_project(projects)
            is_saved = False
        elif choice == "u":
            update_project(projects)
            is_saved = False
        print(MENU)
        choice = input(">>> ").lower()
    if not is_saved:
        print("Would you like to save to projects.txt? no, I think not.")
    print("Thank you for using custom-built project management software.")

def load_projects(file_name):
    """Loaded projects from file and store in a list"""

    projects = []
    in_file = open(file_name, "r")
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

    percentage_choice = get_percentage("New percentage: ")
    priority_choice = get_priority("New priority: ")

    if percentage_choice != "":
        setattr(project, "completion", percentage_choice)
    if priority_choice != "":
        setattr(project, "priority", priority_choice)

def add_project(projects):
    """Add a new project and append to the list"""
    print("Let's add a new project")
    project_name = input("Name: ")
    while project_name == "":
        project_name = input("Name: ")

    is_valid_choice = False
    project_date = input("Start date (dd/mm/yy): ")
    while not is_valid_choice:
        try:
            project_date = datetime.datetime.strptime(project_date, "%d/%m/%Y").date()
            is_valid_choice = True
        except ValueError:
            project_date = input("Start date (dd/mm/yy): ")
    project_date = project_date.strftime("%d/%m/%Y")

    project_priority = get_priority("Priority: ")
    while project_priority == "":
        project_priority = get_priority("Priority: ")

    is_valid_choice = False
    project_cost = input("Cost estimate: $")
    while not is_valid_choice:
        try:
            project_cost = float(project_cost)
            is_valid_choice = True
        except ValueError:
            project_cost = input("Cost estimate: $")

    project_completion = get_percentage("Percent complete: ")
    while project_completion == "":
        project_completion = get_percentage("Percent complete: ")

    project = Project(project_name, project_date, project_priority, project_cost, project_completion)
    projects.append(project)

def filter_projects_by_date(projects):
    is_valid_choice = False
    date = input("Show projects that start after date (dd/mm/yy): ")
    while not is_valid_choice:
        try:
            date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
            is_valid_choice = bool(date)
        except ValueError:
            date = input("Show projects that start after date (dd/mm/yy): ")

    date_year = int(date.strftime("%Y"))
    date_month = int(date.strftime("%m"))
    date_day = int(date.strftime("%d"))

    projects_by_date = []
    for project in projects:
        project_date = datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
        project_date_year = int(project_date.strftime("%Y"))
        if project_date_year > date_year:
            # By year
            projects_by_date.append([project, project_date])
        elif project_date_year == date_year:
            project_date_month = int(project_date.strftime("%m"))
            if project_date_month > date_month:
                # By month
                projects_by_date.append([project, project_date])
            elif project_date_month == date_month:
                project_date_day = int(project_date.strftime("%d"))
                if project_date_day >= date_day:
                    # By day
                    projects_by_date.append([project, project_date])

    projects_by_date.sort(key=itemgetter(1))
    for project in projects_by_date:
        print(project[0])

def save_projects(projects):
    file_name = input("Save to: ")
    while file_name == "":
        file_name = input("Save to: ")

    # write to file
    with open(file_name, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost}\t{project.completion}\n")

def get_priority(prompt):
    is_valid_choice = False
    priority_choice = input(prompt)
    if priority_choice == "":
        is_valid_choice = True
    while not is_valid_choice:
        try:
            priority_choice = int(priority_choice)
            if priority_choice > 0:
                is_valid_choice = True
            else:
                priority_choice = input(prompt)
        except ValueError:
            priority_choice = input(prompt)
    return priority_choice

def get_percentage(prompt):
    is_valid_choice = False
    percentage_choice = input(prompt)
    if percentage_choice == "":
        is_valid_choice = True
    while not is_valid_choice:
        try:
            percentage_choice = int(percentage_choice)
            if -1 < percentage_choice < 101:
                is_valid_choice = True
            else:
                percentage_choice = input(prompt)
        except ValueError:
            percentage_choice = input(prompt)
    return percentage_choice

main()
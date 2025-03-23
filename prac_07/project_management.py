""" 19:56
Project
Estimate: 45 minutes
Actual:    minutes
"""

import datetime
from project import Project

FILE_NAME = "projects.txt"

def main():
    print("Welcome to Pythonic Project Management")
    projects = []
    load_projects(projects)
    print(projects)
    pass

def load_projects(projects):
    in_file = open(FILE_NAME, "r")
    in_file.readline()
    for line in in_file:
        parts = line.split("\t")
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)

main()
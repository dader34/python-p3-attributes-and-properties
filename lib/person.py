#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self,name='J. Doe', job='Sales'):
        approved_jobs = ["Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal", "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"]
        if(type(name) == str and len(name) > 0 and len(name) < 26):
            self.name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")
        if job in approved_jobs:
            self.job = job
        else:
            print("Job must be in list of approved jobs.")

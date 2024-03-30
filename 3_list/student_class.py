#!/usr/bin/env python3

class Student():
    def __init__(self, name, score):
        pass

num_students = input("Enter number of students: ")
num_students = int(num_students)

students = list()
for i in range(num_students):
    name = input("Enter student name: ")
    score = input("Enter {}]s score: ")
    score = int(score)
    s = Student(name, score)
    students.append(s)

# find max score, print student name with max score

# find average score


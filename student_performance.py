import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

print("STUDENT PERFORMANCE ANALYZER")
print(df)

subjects = ['Maths', 'Python', 'DBMS', 'Data_Structures', 'English']

print("\nSTUDENT ANALYSIS")
# Calculate the total and average marks for each student
for index, row in df.iterrows():
    total = sum(row[subject] for subject in subjects)
    average = total / len(subjects)

    print(f"\nName: {row['Name']}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
#calculate grade 
print("\nGRADE AND RESULT")

for index, row in df.iterrows():
    total = sum(row[subject] for subject in subjects)
    average = total / len(subjects)

    if average >= 90:
        grade = 'A+'
    elif average >= 80:
        grade = 'A'
    elif average >= 70:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    elif average >= 50:
        grade = 'D'
    else:
        grade = 'F'

    if average >= 50:
        result = 'PASS'
    else:
        result = 'FAIL'

    print(f"\nName: {row['Name']}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
    print(f"Result: {result}")
#calaculate top performer
print("\nTOP PERFORMER")

top_average = 0
top_student = ""

for index, row in df.iterrows():
    total = sum(row[subject] for subject in subjects)
    average = total / len(subjects)

    if average > top_average:
        top_average = average
        top_student = row['Name']

print(f"Top Student: {top_student}")
print(f"Top Average: {top_average:.2f}")

print("\nGRAPH")
 
averages = []

for index, row in df.iterrows():
    total = sum(row[subject] for subject in subjects)
    average = total / len(subjects)
    averages.append(average)

plt.bar(df['Name'], averages)

plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")

plt.savefig("average_graph.png")
print("\nHIGHEST MARKS")
for subject in subjects:
    highest = df[subject].max()
    print(f"{subject}: {highest}")
print("\nSUBJECT WISE COMPARSION ")
print("\nSUBJECT-WISE COMPARISON")
plt.figure()

plt.bar(df['Name'], df['Maths'], label="Maths")
plt.bar(df['Name'], df['Python'], bottom=df['Maths'], label="Python")
plt.bar(df['Name'], df['DBMS'], bottom=df['Maths'] + df['Python'], label="DBMS")
plt.bar(df['Name'], df['Data_Structures'],
        bottom=df['Maths'] + df['Python'] + df['DBMS'],
        label="Data Structures")
plt.bar(df['Name'], df['English'],
        bottom=df['Maths'] + df['Python'] + df['DBMS'] + df['Data_Structures'],
        label="English")

plt.title("Student Subject-wise Performance")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()

plt.savefig("subject_comparison.png")

pass_count = 0

for index, row in df.iterrows():
    total = sum(row[subject] for subject in subjects)
    average = total / len(subjects)

    if average >= 50:
        pass_count += 1

print("Number of students passed:", pass_count)
plt.show()

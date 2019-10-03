#Nana Osei Asiedu Yirenkyi
#Summer 2018
#In this project, you will act as a student and create a gradebook to keep track of some #of the subjects you've taken and grades you have received in them. To complete the #project, you will need to understand how to create and combine lists, and how to add #elements.


#creates a list of pairs last semester subjects and the corresponding grades
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

#creates a list of this semester's subjects
subjects = ['physics', 'calculus', 'poetry', 'history']

#creates a list of this semester's subjects
grades = [98, 97, 85, 88]

#adds computer science to the list of subjects
subjects.append('computer science')

#adds the computer science grade to the list of grades
grades.append(100)

#creates a list called 'gradebook' which pairs this semester's subjects with their corresponding grades
gradebook = list(zip(subjects, grades))

#adds the subject visual arts and its corresponding grade to the gradebook list
gradebook.append(('visual arts', 93))

#prints the list of this semesters subjects and corresponding grades
print(gradebook)

#combines the list of this semester's subjects and grades to that of last semester 
full_gradebook = last_semester_gradebook + gradebook

#prints the combined list of grades and subjects from both semesters
print('\n',full_gradebook)

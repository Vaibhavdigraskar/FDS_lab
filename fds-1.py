marks = input("input a list of marks ").split()
for n in range(len(marks)):
    marks[n] = int(marks[n])
print(marks)
total_marks = 0
for i in marks:
    total_marks += i
print(total_marks)
  
total_students = 0
for students in marks:
    total_students += 1
print(total_students)

average = str(total_marks / total_students)

print("the average marks are " + average)
      
maxi = marks[0]
for i in range(len(marks)):
    if marks[i] > maxi:
        maxi = marks[i]
print(f"maximum marks are {maxi}")

mini = marks[0]
absent =0
for n in range(len(marks)):
    if marks[n] == -1:
        absent += 1
    if marks[i] < mini:
        mini = marks[i]
print(f"minimum marks are {mini}")
print(f"no. of absebt stud : {absent}")

#maximum freq
u = 0
max = 0
for j in marks:
    if marks.index(j) == u:
        if marks.count(j)>max:
            max = marks.count(j)
    i += 1
print(f"maximum frequency : {max}")
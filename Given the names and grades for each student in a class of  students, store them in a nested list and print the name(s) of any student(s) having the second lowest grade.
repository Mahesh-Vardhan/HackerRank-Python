number_of_students = int(input())
list_of_students = []
for _ in range(number_of_students):
    names = input()
    marks = float(input())
    indi_list = [names, marks]
    list_of_students.append(indi_list)
marks = []
for i in range(number_of_students):
    for j in range(1, 2):
            marks.append(list_of_students[i][j])
            min = list_of_students[i][j]
marks.sort()
set_marks = set(marks)
sorted_marks_list = list(set_marks)
sorted_marks_list.sort()
final_names = []
for i in range(number_of_students):
     for marks in range(1, 2):
          if sorted_marks_list[1] == list_of_students[i][1]:
               final_names.append(list_of_students[i][0])
final_names.sort()
for perlu in final_names:
     print(perlu)
 

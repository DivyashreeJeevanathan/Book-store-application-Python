def calc(marks):
 average_marks = sum(marks) / len(marks) if marks else 0
 max_marks = max(marks) if marks else 0
 min_marks = min(marks) if marks else 0
 return average_marks, max_marks, min_marks
marks = (56, 78, 95, 45, 78, 34, 87, 67, 78, 91)
average, maximum, minimum = calc(marks)
print("8. Marks:", marks)
print(" Average marks:", average)
print(" Maximum marks:", maximum)
print(" Minimum marks:", minimum)

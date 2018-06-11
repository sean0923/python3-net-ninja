

grades = ['A', 'B', 'F', 'C', 'A']

def remove_fail_grade(grade):
  return grade != 'F'

filtered_grade_1 = list(filter(remove_fail_grade, grades))
print('filtered_grade_1: ', filtered_grade_1)

filtered_grade_2 = [grade for grade in grades if grade != 'F']
print('filtered_grade_2: ', filtered_grade_2)

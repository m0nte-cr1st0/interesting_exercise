lloyd = {
      "name": "Lloyd",
      "homework": [90.0,97.0,75.0,92.0],
      "quizzes": [88.0,40.0,94.0],
      "tests": [75.0,90.0]
    }
alice = {
      "name": "Alice",
      "homework": [100.0, 92.0, 98.0, 100.0],
      "quizzes": [82.0, 83.0, 91.0],
      "tests": [89.0, 97.0]
    }
tyler = {
      "name": "Tyler",
      "homework": [0.0, 87.0, 75.0, 22.0],
      "quizzes": [0.0, 75.0, 78.0],
      "tests": [100.0, 100.0]
    }
    
studentsthat = [lloyd, alice, tyler]

for student in studentsthat:
    for data in student:
        print('The student\'s {}: {}'.format(data, student[data]))
    print()

def average(numbers):
    total = float(sum(numbers))
    return total / len(numbers)

def get_average(student):
    homework = average(student['homework'])
    quizzes = average(student['quizzes'])
    tests = average(student['tests'])
    total = [homework*0.1, tests*0.3, quizzes*0.6]
    return sum(total)

def get_letter_grade(score):
    res = ''
    if score >= 90:
        res = "A"
    elif score >= 80: 
        res = "B"
    elif score >= 70: 
        res = "C"
    elif score >= 60: 
        res = "D"
    else: 
        res = "F"
    return res

# Test
# print(get_letter_grade(get_average(lloyd)))

def get_class_average(students):
    global results
    results = []
    for student in students:
        results.append(get_average(student))
        
    return round(average(results), 2)

func = get_class_average(studentsthat)
print('Average score:', func)
print('Average grade:', get_letter_grade(func))
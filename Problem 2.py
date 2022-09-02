dog = dict()
dog['name'] = 'test'
dog['color'] = 'black'
dog['breed'] = 'unknown'
dog['legs'] = 3
dog['age'] = '1'

student = dict()
student['first_name'] = ""
student['last_name'] = ""
student['gender'] = ""
student['age'] = 1
student['marital_status'] = ""
student['skills'] = []
student['country'] = ""
student['city'] = ""
student['address'] = ""

student_dictionary_len = len(student)
print("Student dictionary length: ", student_dictionary_len)

assert type(student['skills']) == list
print("Type of skills is list")

student['skills'].append("C++")
student['skills'].append("Java")

print("dictionary keys as a list: ", student.keys())
print("dictionary values as a list: ", student.values())
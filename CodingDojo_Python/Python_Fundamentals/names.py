# # Part One

# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def studentNames(arr):

# 	for student in students:
# 		output = ''
# 		output2 = '{} {}'.format(student["first_name"], student["last_name"])
# 		print output2

# studentNames(students)


# Part Two

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for group in users:
	print group
	for index in range(len(users[group])):
		print '{} - {} {} - {}'.format(index + 1, users[group][index]['first_name'], users[group][index]['last_name'], len(users[group][index]['first_name']) + len(users[group][index]['last_name'])
print('This is a GPA calculator')
print('Please enter all your letter grades, one by one per line')
print('Enter a blank line to distinigush the end.')

points = {'A+': 4.0, 'A': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.67,
          'C+': 2.33, 'C': 1.67, 'D+': 1.33, 'D': 1.0, 'F': 0.0}

num_course = 0
total_points = 0
done = False
while not done:
    grade = input()
    if grade == '':
        done = True
    elif grade not in points:
        print(f'Unknown grade {grade} will be ignored')
    else:
        num_course += 1
        total_points += points[grade]
    if num_course > 0:
        print('Your GPA is {0:.3}'.format(total_points/num_course))

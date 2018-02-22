students_evaluation_list = [{'school_class': '4a', 'scores': [3, 3, 4, 4, 5]},
                            {'school_class': '5a', 'scores': [3, 4, 4, 5, 5]},
                            {'school_class': '6a', 'scores': [4, 4, 5, 5, 5]}
                            ]

for school_class in students_evaluation_list:
    print(school_class['scores'])
    print(sum(school_class['scores']))
    # total sum per class
    print(len(school_class['scores']))
    # total number of marks
    print(sum(school_class['scores']) / len(school_class['scores']))
    # arithmetic mean value per class

a = [3, 3, 4, 4, 5]
b = [3, 4, 4, 5, 5]
c = [4, 4, 5, 5, 5]

school_marks = a + b + c
print(school_marks)
print(sum(school_marks))
print(len(school_marks))
print(sum(school_marks) / len(school_marks))
# This exercise uses a data structure that stores Udacity course information.
# The data structure format is:

#    { <semester>: { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }


courses = {
    'spring2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'fall2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'spring2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                        'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }


def when_offered(courses, course):
    # TODO: Fill out the function here.
    answer=[]
    for key in courses:
      if course in courses[key]:
        answer.append(key)
# if key1 in c
    # TODO: Return list of semesters here.
    return answer
# for key in courses:
#   courses[key][]
#     print(key)


print(when_offered(courses, 'cs101'))

# Correct result: 
# ['fall2020', 'spring2020']

print(when_offered(courses, 'bio893'))
# Correct result: 
# []

# Answer:
def when_offered(courses, course):
    # TODO: Fill out the function here.
    semesters = []
    for semester in courses:
        if course in courses[semester]:
            semesters.append(semester)
    # TODO: Return list of semesters here.
    return semesters



print(when_offered(courses, 'cs101'))
# Correct result: 
# ['fall2020', 'spring2020']

print(when_offered(courses, 'bio893'))
# Correct result: 
# []

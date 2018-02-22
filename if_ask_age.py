kindergarten = 2
school = 7
university = 17
job = 22

age = int(input('How old are you?'))

if age >= job:
    print("You've got a job.")
elif age < job and age > university:
    print("You are a student.")
elif age < university and age > school:
    print("You are a pupil.")
elif age < school and age > kindergarten:
    print("You are a child.")
else:
    print("You are a baby.")
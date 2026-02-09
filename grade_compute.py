def GradeToNumber(x):
    if x == 'A+':
        x = 4
    elif x == 'A':
        x = 3.8
    elif x == 'A-':
        x = 3.7
    elif x == 'B+':
        x = 3.3
    elif x == 'B':
        x = 3
    elif x == 'B-':
        x = 2.7 
    elif x == 'C+':
        x = 2.3
    elif x == 'C':
        x = 2
    elif x == 'C-':
        x = 1.7
    elif x == 'D+':
        x = 1.3
    elif x == 'D':
        x = 1.0
    elif x == 'F':
        x = 0
    return x
        
def NumberToGrade(x):
    if x == 4:
        x = 'A+'
    elif x < 4 and x > 3.7:
        x = 'A'
    elif x <= 3.7 and x > 3.3:
        x = 'A-'
    elif x <= 3.3 and x > 3:
        x = 'B+'
    elif x <= 3 and x > 2.7:
        x = 'B'
    elif x <= 2.7 and x > 2.3:
        x = 'B-'
    elif x <= 2.3 and x > 2:
        x = 'C+'
    elif x <= 2 and x > 1.7:
        x = 'C'
    elif x <= 1.7 and x > 1.3:
        x = 'C-'
    elif x <= 1.3 and x > 1:
        x = 'D+'
    elif x <= 1 and x > 0:
        x = 'D'
    elif x == 0:
        x = 'F'
    return x
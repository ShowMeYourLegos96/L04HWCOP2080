def GradeToNumber(x):
    if x == 'A+':
        x = 4
    elif x == 'A':
        x = 4
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
        
def NumberToGrade(c):
    
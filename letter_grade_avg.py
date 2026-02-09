from grade_compute import GradeToNumber,NumberToGrade


def MinGrade(**GradeToNumber):
    letter = []
    for i in letter:
        min = GradeToNumber(letter[i])
        if min > GradeToNumber(letter[i+1]):
            min = GradeToNumber(letter[i+1])
        else:
            continue 
        return min

#def ProcessLine(GradeToNumber, NumberToGrade):

#grades = input("Enter the four grades: $  $  $  ")
x1 = "z"
while x1.upper() != "Q":
    x1 = input("What is the first grade? ")
    x2 = input("What is the second grade? ")
    x3 = input("What is the third grade? ")
    x4 = input("What is the fourth grade? ")
    
    y1 = GradeToNumber(x1)
    y2 =GradeToNumber(x2)
    y3 = GradeToNumber(x3)
    y4 = GradeToNumber(x4)

    num_Low = min(y1,y2,y3,y4)

    my_avg =  (y1 + y2 + y3 + y4 - num_Low) / 3
    if NumberToGrade(my_avg) == 'B-' or 'C+' or 'C' or 'C-' or 'D+' or 'D' or 'D-' or 'F':
        new_avg = my_avg + 0.25
    else:
        new_avg = my_avg
    
    d = input("Do you want to continue?: ")
    if d.upper() == "Q":
        break
    
print("Grades entered: ", [x1,x2,x3,x4])
print("Lowest Grade dropped: ", NumberToGrade(num_Low))
print("Calculated Average: ", my_avg)
print("Final Letter Grade: ",NumberToGrade(new_avg))
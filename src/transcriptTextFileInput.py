'''
Created on May 22, 2013

@author: dyc2112
'''
import linecache

#takes a list of credit points and letter grades and calculates the GPA for those pairs
def calculateGpa (points, grades):
    totalPoints = 0
    gradePoints = 0
    gpa = -1
    length = int(len(points))
    if len(points) != len(grades):
        print 'the number of points does not equal the number of grades!'
    
    for index in range(length):
        print 'calculateGPA: index={} points={}, letter2number={}'.format(index, points[index], letter2number(grades[index]))
        totalPoints += points[index]
        print 'points * grade = ', float(points[index])*float(letter2number(grades[index]))
        gradePoints = gradePoints + float(points[index])*float(letter2number(grades[index]))
    print 'totalPoints = ', totalPoints
    print 'gradePoints = ', gradePoints
    gpa = gradePoints/totalPoints
    print 'gpa = ', gpa
    return gpa

#converts a letter grade into a number for calculation
def letter2number (letter):
    letterGrade = str(letter).lower()
    #print 'letter2number: input received = ', letterGrade
    if letterGrade == 'a+':
        return 4.33
    if letterGrade == 'a':
        return 4.00
    if letterGrade == 'a-':
        return 3.67
    if letterGrade == 'b+':
        return 3.33
    if letterGrade == 'b':
        return 3.00
    if letterGrade == 'b-':
        return 2.67
    if letterGrade == 'c+':
        return 2.33
    if letterGrade == 'c':
        return 2.00
    if letterGrade == 'c-':
        return 1.67
    if letterGrade == 'f':
        return 0.00
    if letterGrade in ('r', 'p'):
        return -1
    else:
        return -1
        print 'letter2number: I did not program for a letter grade'

#headingTitle = ['callNum', 'dept', 'number', 'section', 'points', 'title', 'grade']

'''
opens the input.txt file, goes through it line by line to look for where the grades are located
saves the line grades are located in gradeLine
saves the number of glasses in numClasses
saves the number of headers as numHeaders
    each semester has a new line of headers:
        Call#    Dept    Number    Section    Points    Title    Grade

'''
with open('input.txt') as gradeInput:
    with open('log.txt', 'w') as log:
        currentLine = 1
        numClasses = 0
        numHeaders = 0
        gradeLine = []
        
        for line in gradeInput:
            #begin to look for where the grades are
            print 'Line ', currentLine, ':\t', line, '\tline breakdown by tab delimitation:'
            print '\tlength: ', len(line.split('\t'))
            #all the grade grade lines have 7 parts separated by tabs, can be a header or a grade
            if len(line.split('\t')) == 7:
                if line.split('\t')[0].lower() == 'call#': #this is a header
                    print '\tthis is header'
                else: #i found a set of grades!
                    print '\t~~~~~~~~~~ your grades! begin ~~~~~~~~~~'
                    numClasses += 1
                    gradeLine.append(currentLine)
            currentLine += 1
            
            
            #some fancy printouts to locate grade location
            lineIndex = 0
            for word in line.split('\t'):
                if len(line.split('\t')) == 7 and line.split('\t')[0].lower() != 'call#':
                    print '\t~\tLine Index', lineIndex, ': ', word
                else:
                    print '\t\tLine Index', lineIndex, ': ', word
                lineIndex += 1
            if len(line.split('\t')) == 7:
                if line.split('\t')[0].lower() != 'call#':
                    print '\t~~~~~~~~~~ your grades! ends ~~~~~~~~~~ \n'
        gradeInput.seek(0)

print '\n\n\n\n'
#classDpt list stores the unique departments in order of appearance
classDpt = []
numClassDpt = 1
#print 'print classDpt: ', classDpt
for lineNum in gradeLine:
    #gets the entire line where grade information was found (gradeLine)
    line = linecache.getline('input.txt', lineNum)
    print 'line number {:2d}: {}'.format(lineNum, str(line))
    #print 'print classDpt loop: ', classDpt
    if linecache.getline('input.txt', lineNum).split('\t')[1] not in classDpt:
        #print 'i did not find {} in here, so i am adding it'.format(linecache.getline('input.txt', lineNum).split('\t')[1])
        numClassDpt += 1
        classDpt.append(linecache.getline('input.txt', lineNum).split('\t')[1])
print 'final classDpt: ', classDpt

print '\n\nSummary:'
print '{:2d} line(s) read from input.txt'.format(currentLine-1)
print 'you have taken {:2d} class(es) from {:2d} departments'.format(numClasses-numHeaders, numClassDpt)
print 'grades found on lines:', gradeLine

print '\n=========\n'

points = [1.50,5.00]
grades = ['B-', 'B+']
print 'letter2number index 0: ', letter2number(grades[0])

print '\n=========\n'

calculateGpa(points, grades)
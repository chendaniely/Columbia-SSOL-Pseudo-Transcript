'''
Created on Jun 18, 2013

@author: Daniel Chen
'''
import linecache
import Tkinter as tk
import tempfile

#takes a list of credit points and letter grades and calculates the GPA for those pairs
#assumes point-grade pair are in the same index of the 2 lists
def calculateGpa (points, grades):
    totalPoints = 0
    gradePoints = 0
    gpa = -1
    length = int(len(points))
    if len(points) != len(grades):
        print 'the number of points does not equal the number of grades!'
    
    for index in range(length):
        print 'calculateGPA: index={} points={}, letter2number={}'.format(index, points[index], letter2number(grades[index]))
        totalPoints += float(points[index])
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

def guiInput():
    #headingTitle = ['callNum', 'dept', 'number', 'section', 'points', 'title', 'grade']
    validLetterGrades = ['a+','a','a-','b+','b','b-','c+','c','c-','f']
    '''
    opens the input.txt file, goes through it line by line to look for where the grades are located
    saves the line grades are located in gradeLine
    saves the number of classes in numClasses
    saves the number of headers as numHeaders
        each semester has a new line of headers:
            Call#    Dept    Number    Section    Points    Title    Grade
    '''
    with open('inputGUI.txt', 'w') as gradeInput:
        with open('logGUI.txt', 'w') as log: 
            gradeInput.write(e.get())
            currentLine = 1
            numClasses = 0
            numHeaders = 0
            gradeLine = []
            
            for line in gradeInput:
                #begin to look for where the grades are
                print 'Line ', currentLine, ':\t', line, '\tline breakdown by tab delimitation:'
                log.write('Line ', currentLine, ':\t', line, '\tline breakdown by tab delimitation:')
                print '\tlength: ', len(line.split('\t'))
                log.write('\tlength: ', len(line.split('\t')))
                #all the grade grade lines have 7 parts separated by tabs, can be a header or a grade
                if len(line.split('\t')) == 7:
                    if line.split('\t')[0].lower() == 'call#': #this is a header
                        print '\tthis is header'
                        log.write('\tthis is header')
                    else: #i found a set of grades!
                        print '\t~~~~~~~~~~ your grades! begin ~~~~~~~~~~'
                        log.write('\t~~~~~~~~~~ your grades! begin ~~~~~~~~~~')
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
    
    allPoints = []
    allGrades = []
    allGradesConvert = [] #do not need
    
    #print 'print classDpt: ', classDpt
    for lineNum in gradeLine:
        #gets the entire line where grade information was found (gradeLine)
        line = linecache.getline('input.txt', lineNum)
        print 'line number {:2d}: {}'.format(lineNum, str(line))
        #print 'print classDpt loop: ', classDpt
        
        '''
        for every line of classes, see what department the class is from and add it to classDpt if it is unique
        '''
        if linecache.getline('input.txt', lineNum).split('\t')[1] not in classDpt:
            #print 'i did not find {} in here, so i am adding it'.format(linecache.getline('input.txt', lineNum).split('\t')[1])
            numClassDpt += 1
            classDpt.append(linecache.getline('input.txt', lineNum).split('\t')[1])
        
        '''
        for ever line of classes, add the credits and grades to be calculated for overall gpa into separate lists
        if the grade is a 'p' or empty, skip
        '''
        print 'point number pair: ', line.split('\t')[4], line.split('\t')[6]
        if line.split('\t')[6].rstrip('\n').lower() in validLetterGrades:
            allPoints.append(line.split('\t')[4])
            allGrades.append(line.split('\t')[6].rstrip('\n'))
            allGradesConvert.append(letter2number(line.split('\t')[6].rstrip('\n')))
        else:
            continue
            
    print 'final classDpt: ', classDpt
    
    print '\n\nSummary:'
    print '{:2d} line(s) read from input.txt'.format(currentLine-1)
    print 'you have taken {:2d} class(es) from {:2d} departments'.format(numClasses-numHeaders, numClassDpt)
    print 'grades found on lines:', gradeLine

    
    calculateGpa(allPoints,allGrades)

def callback():
    print e.get()
    master.destroy()
    
def on_button():
    with open('inputGUI.txt', 'w') as f:
        f.write(e.get())
        callback()
    #tkMessageBox.showinfo("Tkinter Entry Widget", guiInput())

    
master = tk.Tk()
L1 = tk.Label(master, text="Please Paste in SSOL GPA Page, then click 'Calculate' \n You do not need to see all the pasted contents in the textbox below")
L1.pack()

e = tk.Entry(master)
e.pack()
e.focus_set()

calculateButton = tk.Button(master,width=20, text="Calculate", command=guiInput)
closeButton = tk.Button(master,width=10, text="Close", command=callback)

calculateButton.pack(side = tk.LEFT)
closeButton.pack(side = tk.RIGHT)



tk.mainloop()

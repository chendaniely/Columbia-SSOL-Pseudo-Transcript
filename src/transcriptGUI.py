'''
Created on Jun 18, 2013

@author: Daniel Chen
'''
import linecache
import Tkinter as tk
import tkMessageBox
#import ScrolledText

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
    validLetterGrades = ['a+','a','a-','b+','b','b-','c+','c','c-','f']

    with open('outputGUI.txt') as gradeInput:
        with open('log.txt', 'w') as log:
            currentLine = 1
            numClasses = 0
            numHeaders = 0
            gradeLine = []
            
            for line in gradeInput:
                if len(line.split('\t')) == 7:
                    numClasses += 1
                    gradeLine.append(currentLine)
                currentLine += 1

                lineIndex = 0
                
                for word in line.split('\t'):
                    lineIndex += 1
                gradeInput.seek(0)
    
    classDpt = []
    numClassDpt = 1
    
    allPoints = []
    allGrades = []
    allGradesConvert = []
    
    for lineNum in gradeLine:
        line = linecache.getline('input.txt', lineNum)
        if linecache.getline('input.txt', lineNum).split('\t')[1] not in classDpt:
            numClassDpt += 1
            classDpt.append(linecache.getline('input.txt', lineNum).split('\t')[1])
            
        if line.split('\t')[6].rstrip('\n').lower() in validLetterGrades:
            allPoints.append(line.split('\t')[4])
            allGrades.append(line.split('\t')[6].rstrip('\n'))
            allGradesConvert.append(letter2number(line.split('\t')[6].rstrip('\n')))
        else:
            continue
                
    print '\n\nSummary:'
    print '{:2d} line(s) read from input.txt'.format(currentLine-1)
    print 'you have taken {:2d} class(es) from {:2d} departments'.format(numClasses-numHeaders, numClassDpt)
    print 'grades found on lines:', gradeLine
    print allPoints
    print allGrades
   
    calculateGpa(allPoints,allGrades)

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="Get", command=self.on_button)
        self.button.pack()
        self.entry.pack()

    def on_button(self):
        #global self.entry 
        with open('outputGUI.txt', 'w') as f:
            f.write(self.entry.get())
        print self.entry.get()
        tkMessageBox.showinfo("Tkinter Entry Widget", guiInput())

app = SampleApp()
app.mainloop()
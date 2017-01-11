
#Change the a sentence to another sentence, letter by letter.
#The sentences will always have the same length.
import sys

inputA = sys.argv[1]
inputB = sys.argv[2]

if (len(inputB) == len(inputA)):
    counter = len(inputA) 
    print inputA
    for x in range(0,counter):
        listA = list(inputA)
        listB = list(inputB)
        listA[x] = listB[x]
        inputA = ''.join(listA)
        print inputA

else:
    print 'ERROR: Two sentences do not have same length'

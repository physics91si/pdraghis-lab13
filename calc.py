#!/usr/bin/python

# Lab 13
# Physics 91SI
# Spring 2016

import sys

def main():
    """Join command-line arguments and pass them to unitcalc(), then print."""
    calculation = ''.join(sys.argv[1:])
    print calc(calculation)



def calc(s):
    """Parse a string describing an operation on quantities with units."""   
    l=[]
    operations=[]
    numbers=[]
    for i in range(len(s)):
        l.append(s[i])
    for i in range(len(l)):
        if l[i].isdigit():
            numbers.append(i)
        else:
            operations.append(i)
    if len(numbers)==0:
        return "You didn't introduce any numbers"
    if len(operations)==0:
        return "You didn't introduce any operation"

        result=c(create_number(s[0:int(operations[0])]),create_number(s[int(operations[0])+1:]),s[operations[0]])
        
    if len(operations)>1:
        result=c(create_number(s[0:int(operations[0])]),create_number(s[int(operations[0]+1):int(operations[1])]),s[operations[0]])
        for i in range(1,len(operations)-1):
            result=c(result,create_number(s[operations[i]+1:operations[i+1]]),s[operations[i]])
        result=c(result,create_number(s[operations[-1]+1:]),s[operations[-1]])
    else: 
         result=c(create_number(s[0:int(operations[0])]),create_number(s[int(operations[0])+1:]),s[operations[0]])
    return result            

    
def c(num1, num2, operation):
    if operation=='+':
        return num1+num2
    elif operation=='-':
        return int(num1)-int(num2)
    elif operation=='*':
        return int(num1)*int(num2)
    elif operation=='/':
        return int(num1)/int(num2)

def create_number(string):
    
    result=0
    for i in range(len(string)):
        result=result+int(string[i])*10**(len(string)-i-1)
    return result

if __name__ == "__main__": main()

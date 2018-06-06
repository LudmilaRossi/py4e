"""
In this assignment you will read through and parse a file with text and numbers. You will extract all 
the numbers in the file and compute the sum of the numbers.
The sum for the sample text above is 27486. The numbers can appear anywhere in the line. There can be 
any number of numbers in each line (including none).
Handling The Data:
The basic outline of this problem is to read the file, look for integers using the re.findall(), 
looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and 
summing up the integers.
"""
import re
#Extracting Digits and Summing them
hand = open('regex_sum_86503.txt')
numlist = list()

for line in hand:
    line = line.rstrip()
    stuff = re.findall('([0-9]+)', line)
    
    if len(stuff) < 1 : continue

    for i in range(len(stuff)):
        num = int(stuff[i])
        numlist.append(num)

print(sum(numlist))

"""
Optional: Just for Fun
There are a number of different ways to approach this problem. While we don't recommend trying to write 
the most compact code possible, it can sometimes be a fun exercise. Here is a a redacted version of 
two-line version of this program using list comprehension:

Python 2
import re
print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )

Python 3:
import re
print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
"""
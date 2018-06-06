"""
Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Award time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to 
do the computation of time-and-a-half in a function called computepay() and use the function to
do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per 
hour to test the program (the pay should be 498.75). You should use input to read a string and 
float() to convert the string to a number. Do not worry about error checking the user input unless
you want to - you can assume the user types numbers properly. Do not name your variable sum or 
use the sum() function.
"""

def computepay(h,r):
    if h > 40:
        pay = 40 * r + (h-40) * r * 1.5
    else:
        pay = h * r
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

h = float(hrs)
r = float(rate)

p = computepay(h,r)
print(p)
    
"""
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters 
anything other than a valid number catch it with a try/except and put out an appropriate message 
and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
"""

largest = None
smallest = None

while True:
    num = input('Enter a number: ')
    if num == 'done':
        break

    try:
        rnum = int(num)
        if largest is None:
            largest = rnum
        elif rnum > largest:
            largest = rnum

        if smallest is None:
            smallest = rnum
        elif rnum < smallest:
            smallest = rnum 
    except:
        print('Invalid input')
    continue

print('Maximum is', largest)
print('Minimum is', smallest)  

#-----------------

text = "X-DSPAM-Confidence:    0.8475";
tpos = text.find('0')
spos = text.find('5')
host = text[tpos:spos+1]
fhost = float(host)
print(fhost)    

"""
Write a program that prompts for a file name, then opens that file and reads through
the file, and print the contents of the file in upper case. Use the file words.txt 
to produce the output below.
"""

# Use words.txt as the file name
fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

for line in fh:
    line = line.rstrip()
    print(line.upper())

"""
Write a program that prompts for a file name, then opens that file and reads through 
the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and 
compute the average of those values and produce an output as shown below. 

#output:
#Average spam confidence: 0.750718518519

# Updated assignment asks users to not use sum() function or variable name in their solution
# Use the file name mbox-short.txt as the file name """

fname = input('Enter file name: ')
    
fh = open(fname)
count = 0
total = 0
avg = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    num = float(line[21:])
    total = num + total
avg = total / count
print('Average spam confidence:', avg)
    
    
"""
Open the file romeo.txt and read it line by line. For each line, split the line into a 
list of words using the split() method. The program should build a list of words. For 
each word on each line check to see if the word is already in the list and if not append 
it to the list. When the program completes, sort and print the resulting words in 
alphabetical order.
romeo.txt
"""

fname = input('Enter file name: ')
fh = open(fname)
lst = list()

for line in fh:
    line = line.rstrip().split() #Metodo separador. Retorna: una lista con todos elementos 
                                 # encontrados al dividir la cadena por un separador.
    for w in line:
        if not w in lst: 
            lst.append(w)
lst.sort()
print(lst)
    

"""
Open the file mbox-short.txt and read it line by line. When you find a line that starts 
with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line 
(i.e. the entire address of the person who sent the message). Then print out a count at 
the end.
Hint: make sure not to include the lines that start with 'From:'.
"""   
fname = input('Enter file name: ')
fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[1])
    count = count + 1

print('There were', count, 'lines in the file with From as the first word')


"""
Write a program to read through the mbox-short.txt and figure out who has the sent the 
greatest number of mail messages. The program looks for 'From ' lines and takes the second 
word of those lines as the person who sent the mail. The program creates a Python dictionary
that maps the sender's mail address to a count of the number of times they appear in the 
file. After the dictionary is produced, the program reads through the dictionary using a 
maximum loop to find the most prolific committer.
"""
    
name = input('Enter file:')
if len(name) < 1 : name = handle
handle = open(name)

words = list()
for line in handle:
    if not line.startswith('From:') : continue
    line = line.split()
    words.append(line[1])

counts = dict()
for word in words:
    counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None

for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
   

"""
Write a program to read through the mbox-short.txt and figure out the distribution by hour 
of the day for each of the messages. You can pull the hour out from the 'From ' line by 
finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as 
shown below.
"""

name = input('Enter file:')
if len(name) < 1 : name = handle
handle = open(name)

counts = dict()
for line in handle:
    if line.startswith('From '):
        time = line.split()[5].split(':')
        counts[time[0]] = counts.get(time[0], 0) + 1
        
words = list()
for key,value in counts.items():
    words.append( (key,value) )
words.sort()

for hour, counts in words:
    print(hour,counts)

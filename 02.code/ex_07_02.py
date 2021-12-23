#7.2 Write a program that prompts for a file name,
#then opens that file and reads through the file,
#looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values
#from each of the lines and compute the average of those values
#and produce an output as shown below. Do not use the sum()
#function or a variable named sum in your solution.
#You can download the sample data at
#http://www.py4e.com/code3/mbox-short.txt when you are testing below
#enter mbox-short.txt as the file name.


#fname = input("Enter file name: ")
#fh = open(fname,'r')

#for element in fh:
#    element = element.rstrip()
#    print(element.upper())

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)


countLine = 0
countNumbers = 0
for line in fh:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence") :
        strippedLine = line.strip("X-DSPAM-Confidence: ")
        #continue
        countNumbers = countNumbers + float(strippedLine)
        countLine = countLine + 1

        # count = 27
        #countLines = str(count)
##print('Line count:', count)
#print('Line count:' + count)
    #print(line)
        #pos = line.find(' ')
        #slicedValue = line[20:27]
        #slicedValue2 = slicedValue.strip()
        #f_slicedValue = float(slicedValue2)
        #print(f_slicedValue)
print('Average spam confidence:',countNumbers/countLine)
#print("Done")

#text = "X-DSPAM-Confidence:    0.8475";
#pos = text.find(' ')
#slicedValue = text[pos:]
#f_slicedValue = float(slicedValue)
#print(f_slicedValue)

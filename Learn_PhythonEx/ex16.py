from sys import argv

script ,filename = argv

print "We're going to erase %r. " % filename
print "If you don't want this, hit CTRL-C(^C). "
print "If you want this, hit RETURN. "

raw_input("?") #读取输入字符串“？”

print "Opening the file..."
target = open(filename, 'w') #  define target,write file

print  "Truncating the  file. Goodbye! "
target.truncate()  #truncate target

print "Now I'm going to ask you for three lines. "

line1 = raw_input("line 1 : ")
line2 = raw_input("line 2 : ")
line3 = raw_input("line 3 : ")

print "I'm going to write these to the file. "

target.write(line1) #write file in test.txt
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()  # save and close test.txt

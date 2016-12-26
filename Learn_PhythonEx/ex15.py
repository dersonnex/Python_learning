from sys import argv

script, filename = argv #line1-3 to get a filename

txt = open(filename) #command open

print "Here's your file %r:" % filename
print txt.read() # function on txt named read

print "type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
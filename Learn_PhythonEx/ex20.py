#  coding:utf-8
from sys import argv

script, input_file = argv

def  print_all(f):      # define a function named print_all
	print f.read()      # read file

def rewind(f):           # define function named rewind
    f.seek(0)            # back to file 用于移动文件读取指针到指定位置，默认值为0,表示从文件开头算起

def print_a_line(line_count, f): # define a function
    print line_count, f.readline()

current_file = open(input_file)  # use this arugment to open file

print "First let's print the whole file:/n" 

print_all(current_file)

print "Now, let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print the three lines:"

current_file = 1
print_a_line(current_file, current_file)

current_file = current_file + 1
print_a_line(current_file, current_file)

current_file = current_file + 1
print_a_line(current_file, current_file)
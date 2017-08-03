# this one is like your scripts with argv
def print_two(*args):
 arg1, arg2 = args
 print "arg1: %r, arg2: %r" % (arg1, arg2)

 # ok, that *args is actually pointless, we can just do this "函数结束位置一定要取消缩进，要不后面函数命名默认在前一函数命名中
def print_two_again(arg1, arg2):  #多个参数用逗号隔开
 	print "arg1: %r, arg2: %r " % (arg1, arg2)

 # this just takes one argument
 
def print_one(arg1):
     print "arg1: %r " % arg1

 #	this one take no arguments
def print_none():
 	 print "I got nothin'. "

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
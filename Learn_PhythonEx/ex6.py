x= "There are %d types of people." % 10 # defines veriable X 
binary = "binary" # defines veriable binary
do_not = "don't" # defines veriable do_not
y = "Those who know %s and those who %s." % (binary, do_not) # defines veriable y

print x
print y

print "I said: %r." % x  #I said :there are 10 types of people.
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so fanny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e
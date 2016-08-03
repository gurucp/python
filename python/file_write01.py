from sys import argv

script, filename = argv

print "We are going to delete the content of your file %r" % filename
print "If you do not want to delete the content of your file please do Ctrl+C"
print "Else please hit Enter "

raw_input("?")

txt = open(filename, 'w')
print "Truncating the file:"

txt.truncate()

print "Please write three lines to the file:"

line1 = raw_input('>')
line2 = raw_input('>')
line3 = raw_input('>')


print "I am going to write your three lines to %r file:" % filename

#txt.write( '%s \n %s \n %s \n % (line1, line2, line3)')
txt.write('%s \n %s \n %s \n' % (line1, line2, line3))


print "Finally I will save the file"

txt.close()

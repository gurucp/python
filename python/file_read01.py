from sys import argv

script, filename = argv

print "Hi here is your file %r content" % filename

txt = open(filename)

print txt.read()

from sys import argv
script, filename = argv

print "your file name %r " % filename 

txt = filename.open('w+')
in_file = txt.write('testing')


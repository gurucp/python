from sys import argv

script, txt = argv

def file_print(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

filename = open(txt)
print "First let us print whole file:"
file_print(filename)


print "Let us rewind the file"
rewind(filename)

print "Print 3 Lines from the file:"
line_count = 10
print_a_line( line_count, filename)
line_count = 15
print_a_line( line_count, filename)
line_count = line_count+1
print_a_line( line_count, filename)


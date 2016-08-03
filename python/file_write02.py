from sys import argv
from os.path import exists

script, in_file, out_file = argv

print "Copying %s file to %s file" % (in_file, out_file)

print "Reading file %r" % in_file

input_file = open(in_file)
indata = input_file.read()

print "your source file %s is %d byte long" % ( in_file, len(indata))

print "Does file exists???? %r" % exists(out_file)
print "Hit Return to contunue or hit Ctrl+C"
raw_input('>')

output_file = open(out_file, 'w')
output_file.write(indata)

print "Finally closing the file"

output_file.close()
input_file.close()




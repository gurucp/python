def print_three(*args):
    arg1, arg2, arg3 = args
    print "arg1: %r, arg2: %r, arg3: %r" % (arg1, arg2, arg3)
def print_two(arg1, arg2):
    print "arg1: %s, arg2: %s" % (arg1, arg2)
    
def print_nothing():
    print "I am not going totake any arg:)..fuck yourself:"

print_three("guru", "Chaya", "Niyati")
print_two('Chaya', 'Guru')
print_nothing()



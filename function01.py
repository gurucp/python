def print_two(*args):

    arg1, arg2 = args
    print "arg1: %s. arg2: %s" % (arg1, arg2 )

def print_two_again(arg1, arg2):
    print "arg1: %s. arg2: %s" % (arg1, arg2 )

def print_one_arg(arg1):
    print "arg1: %s" % arg1

def print_none():
    print "Print nothing !!!!:))"

print_two("Guru", "Prasad")
print_two_again("Chaya", "Hebbar")
print_none()

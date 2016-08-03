from sys import argv

script, user_name = argv
prompt = '>'

print "Hi %s, I am the script %s" % (script, user_name)
print "Hi %s, I would like to ask you a few questions" % user_name
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
place = raw_input(prompt)

print "What kind of computer do you have %s?" % user_name 
comp = raw_input(prompt)

print """
Allright, you said %r about liking me.
You live in %r place .. I really do not know where it is .."
You told you use %r type of computer ..that is good..
""" % (likes, place, comp) 

__author__ = 'mosassy'

def open_me(new_file):
    try:
        with open(new_file, 'r') as f:

            print f.read()

    except IOError:
        print "Error will robinson"

def open_next(new_file):

    with open(new_file, 'r') as f:

            print f.read()
try:
    open_me("pigsfly.txt")

    open_next("pigsfly.txt")

except IOError:
    print "Um, you messed up dude!"

__author__ = 'mosassy'
import random
import string


n = int(10)
random = ''.join(random.SystemRandom().choice(string.uppercase + string.digits) for _ in xrange(n))
print random

random_string = open("exercise_five.dat", "w+")

random_string.write(random)



import collections

c = collections.Counter()
with open('exercise_five.dat', 'rt') as f:
    for line in f:
        c.update(line.rstrip().lower())

print 'Most common:'
for letter, count in c.most_common():
    print '%s: %7d' % (letter, count)
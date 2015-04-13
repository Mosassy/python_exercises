__author__ = 'mosassy'

def get_input(message):
    try:
        user_input = str(input(message))
        if user_input.isdigit() and user_input is not "0":
            return user_input
        elif user_input is "0":
            print("Cannot be 0!")
        return None
    except NameError:
        print("That doesn't seem to be a number.")
        return None

mph = None

while mph is None:
    mph = get_input("Please input your miles per hour: ")
    if mph is not None:
        mph = float(mph)

meters = mph * 1609.34
barleycorns = (meters * 117.647)/24
furlongs = ((mph*1760)/220)/336
mach = mph / 760.5583
speed_of_light = mph /670616629.3844






print "You traveled %.2f miles per hour" % (mph)
print "You traveled %.2f meters per hour" % (meters)
print "You traveled %.2f barleycorns per day" % (barleycorns)
print "You traveled %.2f furlongs per fortnight" % (furlongs)
print "You traveled %.4f Mach"% (mach)
print "You traveled %.8f percent of the speed of light!"% (speed_of_light)
print "thanks for playing!"





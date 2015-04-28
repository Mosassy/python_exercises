__author__ = 'mosassy'

weather = {
    "Boston": "0 C",
    "Boise": "48 F",
    "Phoenix": "85 F",
    "Miami": "40 C",
    "Riverside": "30 C",
    "Baltimore": "32 F"
    }

def c2f(ctemp):
    return ctemp * 9/5 +32

def f2c(ftemp):
    return (ftemp - 32) * 5/9


def converted(temps_dict):
    for city, temps in temps_dict.items():
        split_degree = temps.split(' ')


        if "C" in split_degree[1]:
            degree = int(split_degree[0])
            conversion_to_f = c2f(degree)
            f = str(conversion_to_f)
            c = degree
            #print degree
            #print f
            print "In %s it is %s degrees Celsius, \n\t which is equivalent to %s degree Fahrenheit" % (city, c, f)
        elif "F" in split_degree[1]:
            degree = int(split_degree[0])
            conversion_to_c = f2c(degree)
            c = str(conversion_to_c)
            f = degree
            print "In %s it is %s degrees Farenheit, \n\t which is equivalent to %s degree Celcius" % (city, f, c)


converted(weather)
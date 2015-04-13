__author__ = 'mosassy'
gallons = raw_input("How many gallons of gas did you use?")

gallons = float(gallons)

if gallons == 0:
    gallons = raw_input("Please insert a number other than zero")
gallons = float(gallons)

liters = gallons * 3.7854
barrel = gallons / 19.5
pounds_co2 = gallons * 20
ethanol_btu = gallons * 75700
cost = gallons * 4

print "You purchased %.2f of gas" % (gallons)
print "You used %.2f liters of gas" % (liters)
print "You produced %.2f pounds of CO2" % (barrel)
print "If you used ethanol you could have used %.2f bBTUs" % (ethanol_btu)
print "You spent %.2f US dollars for your gas"% (cost)
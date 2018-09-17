print("****SlopeCalculator****")

x1 = input("Input x1: ")
y1 = input("Input y1: ")

x2 = input("Input x2: ")
y2 = input("Input y2: ")

print("Your 1st point is (%s" % x1 + " , %s" % y1 + ")")
print("Your 2nd point is (%s" % x2 + " , %s" % y2 + ")")

rise = x2-x1
run = y2-y1
slope = float(x2 - x1)/(y2-y1)

print("Your rise is %s" % rise)
print("Your run is %s" % run)
print("Your slope is %s" % slope)








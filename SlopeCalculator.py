import os
print("****SlopeCalculator****")

bool = 1
n = 0
yes = "yes"
no = "no"

q = input("Would you like sound")
if q in ['yes']:
    n = 1

if q in ['no']:
	n = 0


bool = n	
if bool == 1: 
	os.system("say Hello, Welcome to the slope calculator. You have chosen to have sound Accessibility")


if bool ==1: 
	os.system("say Please input x1")
x1 = input("Input x1: ")
if bool ==1: 
	os.system("say Please input x2")
y1 = input("Input y1: ")

if bool ==1: 
	os.system("say Please input x2")
x2 = input("Input x2: ")
if bool ==1: 
	os.system("say Please input y2")
y2 = input("Input y2: ")


print("Your 1st point is (%s" % x1 + " , %s" % y1 + ")")
print("Your 2nd point is (%s" % x2 + " , %s" % y2 + ")")

rise = x2-x1
run = y2-y1
slope = float(y2-y1)/(x2-x1)
sound = string(slope)

print("Your rise is %s" % rise)
print("Your run is %s" % run)
print("Your slope is %s" % slope)
if bool ==1: 
	os.system("say sound")








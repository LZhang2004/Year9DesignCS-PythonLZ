#loop structure
#COUNT, CHECK, CHANGE
for i in range(0, 6, 1):
	print(i)
# i= 0, 0> 6, True RN LOOP .....
# i = 2, i = 3, ....
#i = 6, 6 < 6, FALSE exit loop

print ("*******")
print("loop that will print 7-104 inclusive")
for i in range(7, 105, 1):
	print(i)
print("*****")

for i in range(3, 0, -1):
	print(i)

print("******")
for i in range(101, -1, -1):
	print(i)

s = "Fish Food"
for i in range(0,len(s),1):
	print(s[i])

for i in range(len(s) -1, -1, -1):
	print(s[i])

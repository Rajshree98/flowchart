import turtle
import csv
import numpy as np
from array import *
wn=turtle.Screen()
turtle.screensize(canvwidth=15000, canvheight=15000, bg=None)
n=6
x=""
q=1
y1="yes"

# with open('info.csv','r') as csv_file:
# 	csv_reader=csv.reader(csv_file)


l1=[]
l2=[]

l1=np.asarray(l1)
l2=np.asarray(l2)



y=-314.28
#dict ={'result':[{1:(0,-84.5)}]}
dict={1:(0,-84.5)}
for p in range(1,n):
	#next_value={p+1:(0,-84.5+y*p)}
	#dict['result'].append(next_value)
	#dict.items()
	dict[p+1]=(0,-84.5+y*p)
#print (dict)
#print dict.items()
	#dict{}.append(next_value)
#print dict

c={1:(110,-84.5)}
for s in range(1,n):
	c[s+1]=(110,-84.5+y*s)

#print(c)

d1={1:(12,-622.56)}
for v in range(1,n):
	d1[v+1]=(12.5,-622.56+y*v)

#print(d1)

#t=-410
#t=-680.3
#d={1:(14,-208.28)}
#d={1:(14,-84.5)}
#for p in range(1,n):
#	d[p+1]=(14,-84.5+t*p)


turtle.circle(50)
turtle.right(90)
turtle.left(180)
turtle.penup()
turtle.forward(45)
turtle.write("start", True, align="center")
turtle.pendown()


turtle.penup()
turtle.backward(45)
turtle.left(180)
turtle.pendown()
	



def rectangle():
	
	
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(100)
	
	turtle.left(90)
	turtle.forward(-75)

	

	turtle.right(90)
	turtle.forward(-200)

	turtle.right(90)
	turtle.forward(-75)

	turtle.left(90)
	turtle.forward(100)
	turtle.penup()
	turtle.right(90)
	turtle.forward(75)
	turtle.pendown()
	turtle.forward(50)
	#turtle.forward(50)
	#turtle.write("Done",True,align="center")
	return "rectangle";



def rhombus():
	
	turtle.right(135)
	turtle.backward(80)
	turtle.left(90)
	turtle.forward(80)
	turtle.right(90)
	turtle.forward(80)
	turtle.right(90)
	turtle.forward(80)
	turtle.penup()
	turtle.backward(80)
	turtle.right(45)
	turtle.forward(45)
	turtle.pendown()
	turtle.write("DONE",True,align="center")
	turtle.penup()

	#turtle.forward(54)
	#turtle.pendown()
	#turtle.forward(30)
	#turtle.write("NO")
	#turtle.forward(40)
	#turtle.left(90)
	#turtle.forward(450)
	#turtle.left(90)
	#turtle.forward(10)

	#turtle.penup()
	#turtle.right(180)
	#turtle.forward(10)
	#turtle.right(90)
	#turtle.forward(450)
	#turtle.right(90)
	#turtle.forward(85)



	#if condition is satisfied
	turtle.right(90)
	turtle.forward(55)
	#turtle.left(45)
	turtle.pendown()
	turtle.forward(26)
	#turtle.write("  YES")

	return "rhombus";


def end():
	#turtle.penup()
	#turtle.forward(210)
	#turtle.right(90)
	#turtle.forward(5)
	#turtle.left(90)
	#turtle.pendown()
    
	turtle.forward(50)
	turtle.right(90)
	turtle.circle(25)
	turtle.right(90)
	turtle.left(180)
	turtle.penup()
	turtle.forward(30)
	turtle.write("END", True, align="center")
	turtle.pendown()
	turtle.penup()
	turtle.forward(20)
	turtle.pendown()
	turtle.forward(50)




def label(x):

	#for q in range(1,n+1):
		var3=dict.get(i)
		turtle.penup()
		turtle.goto(var3)
		turtle.pendown()
		# for line in csv_reader:
		# 	turtle.write("line",True,align="center")
		turtle.write("Stage ",True,align="center")
		turtle.write(i,True)

		turtle.penup()
		turtle.forward(210)
		turtle.right(90)
		turtle.forward(5)
		turtle.left(90)
		turtle.pendown()
 
		
for i in range(1,n+1):

	if(i%2==0):
		y1="yes"
	else:
		y1="no"
	
	if y1=="yes":
		rectangle()
		rhombus()
	
	elif(i!=1 and y1=="no"):
		
		rectangle()
		rhombus()
		turtle.penup()
		turtle.right(180)
		turtle.forward(83.14)
		turtle.right(90)
		turtle.forward(57.14)
		turtle.pendown()
		turtle.write("NO",True)
		turtle.forward(100+10*(i-1))
		turtle.left(90)

		#for a in range(i):
		#	for d in range(i):
		#		if(l1[a]==l2[d]):
		#			turtle.forward(458+308.28*a)
		
		turtle.forward(458)
		turtle.left(90)
		turtle.goto(c.get(i-1))

	
		turtle.penup()
		turtle.left(90)
		turtle.goto(d1.get(i-1))
		#turtle.forward(100)
		#turtle.left(90)
		#turtle.forward((232.14*i)+82.14)
		#turtle.forward(314.28)
		#turtle.right(90)
		#turtle.forward(100)
		#turtle.left(90)
		turtle.pendown()




 		
	else:
		rectangle()
		rhombus()
		#end()

for i in range(1,n+1):
	
	if(y1=="yes"):
		label(x)
	
	elif(i==1 and y1=="no"):
		label(x)
	
	else:
		label(x);
	
end()	

wn.exitonclick()




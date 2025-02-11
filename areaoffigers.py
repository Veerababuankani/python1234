##area of the circle
print("="*50)
print("\t\t\t\t circle")
print("="*50)
r=float(input("enter the radius of the circle:"))
area=3.14*r*r
print("="*50)
print("radius=",r)
print("area of the circle=",round(area,2))
print("="*50)
##area of rectangle and perameter of a rectangle
print("\t\t\t\t rectangle")
print("="*50)
l=float(input("enter the length of the rectangle:"))
b=float(input("enter the breath: of the rectangle:"))
area1=l*b
per=2*(l+b)
print("perameter of a rectangle:{}".format(round(per,2)))
print("area of a rectangle:{}".format(round(area1,2)))
print("="*50)
#squares
print("\t\t\t\tsquare")
print("="*50)
s=float(input(("enter the side of the sqaure:")))
area2=s*s
per2=4*s
print("perameter of the square:{}".format(round(per2,2)))
print("are of the sqaure:{}".format(round(area2,2)))
print("="*50)
#triangle
print("\t\t\t\ttriangle")
print("="*50)
h1=float(input("enter the height of triangle:"))
b1=float(input("enter the breadth of triangle:"))
a=float(input("enter the 1 side of the triangle:"))
b=float(input("enter the 2 side of the triangle:"))
c=float(input("enter the 3 side of the triangle:"))
s=(a+b+c)/2
d1=0.5*(s*(s-a)*(s-b)*(s-c))
print("are of triangle{}".format(d1))
print("the perameter of the triangle:{}".format(round((1/2)*b1*h1)))
print("="*50)
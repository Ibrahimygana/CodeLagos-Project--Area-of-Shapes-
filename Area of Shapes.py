
#Program to calculate area of a user selected shape.

Shape=int(input("Choose a shape: \n1.Circle \n2.Triangle \n3.Square \n" ))
if(Shape==1):
    Radius=int(input("Input your radius: "))
    Area=3.142*Radius**2
    print("The area of your Circle is", Area)
elif(Shape==2):
    Base=int(input("Input your base: "))
    Height=int(input("input your height: "))
    Area=0.5*Base*Height
    print("The area of your Triangle is",Area)
elif(Shape==3):
    Base=int(input("input your base: "))
    Area=Base**2
    print("The area of your square is",Area) 

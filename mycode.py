def squareArea():
    s = float(input("Enter side length of square: "))
    print("Area of Square is: ", s*s)
    

def circleArea():
    r = float(input("Enter radius of circle: "))
    print("Area of Circle is: ", 3.14*r*r)
    
if __name__=="__main__":
    while(1):
        selection = int(input("Enter 1 for Square and 2 for Circle: "))
        if(selection==1):
            squareArea()
            break
        elif(selection==2):
            circleArea()
            break
        else:
            print("Invalid input try again.")
            continue

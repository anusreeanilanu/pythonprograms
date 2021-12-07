def cuboid():
    a=int(input("enter the length of the cuboid"))
    b=int(input("enter the breadth of the cuboid"))
    c=int(input("enter the height of the cuboid"))
    area=2*((a*b)+(a*c)+(b*c))
    print("area=",area)
    p=4*(a+b+c)
    print("perimeter=",p)

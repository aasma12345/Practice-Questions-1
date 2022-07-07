

# car=int(input("enter the CAR time: "))
# bike=int(input("enter the BIKE time: "))
# if car==bike:
#     print("SAME")
# elif car<bike:
#     print("CAR")
# else:
#     print("BIKE")

def time(x,y):
    i=1
    while i<=1:
        if x==y:
            print("SAME") 
        if x<y:
            print("CAR")
        if x>y:
            print("BIKE")
        i=i+1
time(int(input("enter the car: ")),int(input("enter the bike: ")))
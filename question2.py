# def battery(x):
#     i=0
#     a=[]
#     while i<len(x):
#         if x[i]<=15:
#             a.append(x[i])
#             print("yes")
#         else:
#             a.append(x[i])
#             print("no")
#         i=i+1
# battery([15,3,65])


list=[15,3,65]
i=0
while i<len(list):
    if list[i]<=15:
        print("yes")
    else:
       print("no")
    i=i+1

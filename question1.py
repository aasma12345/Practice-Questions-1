list=[85,25,65,21,84]
i=0
while i<len(list):
    a=list[i]%10
    i=i+1
    print(a)
if a%10==0:
    print("yes")
else:
    print("no")
    








#  def isDivisible(arr, n) :
 
#     # Last digit of the last element
#     lastDigit = arr[n - 1] % 10
 
#     # Number formed will be divisible by 10
#     if (lastDigit == 0) :
#         return True
 
#     return False
 
# # Driver code
# if _name_ == "_main_" :
 
#     arr = [ 12, 65, 46, 37, 99 ]
#     n = len(arr)
 
#     if (isDivisible(arr, n)) :
#         print("Yes")
#     else :
#         print("No")
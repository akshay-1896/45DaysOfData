n1 = int(input("Enter the number 1: "))
n2 = int(input("Enter the number 2: "))
n3 = int(input("Enter the number 3: "))

out1 = n1 % n2
out2 = n2 ** n1
print(out1)
print(out2)

n1 += 2
n1 -= 2
n1 *= 2
n1 /= 2
n1 //= 2
n1 **= 2
n1 = n1 + 2
print(n1)

if n1 > n2: 
    print(n1, "is greater than", n2)

elif n2 > n3:
    print(n2, "is greater than", n3)

else :
    print(n3, "is greater than", n2, "and", n1)

# LOGICAL OPERATORS

if n1 > n2 and n1 > n3:
    print(n1, "is greater than", n2, "and", n3)

elif n2 > n1 and n2 > n3:
    print(n2, "is greater than", n1, "and", n3)

else:
    print(n3, "is greater than", n1, "and", n2)
    
# MEMBERSHIP OPERATOR

guest_list = ['Krishna', "Akshay", "Vinay", "Shubham"]

if "Vinay" in guest_list:
    print("\"WELCOME\"")
else:
    print("NOT ALLOWED")

if "Manish" not in guest_list:
    print("NOT ALLOWED")
else:
    print("\"WELCOME\"")




























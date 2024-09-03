

# for i in range(0,10,2):
#     print(f"Hello World {i}")

# i = 0
# while (i <= 10):
#     print(f"Hello World {i}")
#     i += 1

# count = 0
# for i in range(10):
#     count += 1
#     continue
#     print(f"Hii {i}")

# print(count)

ls = [52,41,85,63,96,5,7,45,86,85,6,9,12,36,72,11,22,33]
# count = 0
# temp = 0
# for item in ls:
#     if item == 85:
#         temp += 1
#     if temp == 2:
#         print(f"present at {count}")
#         break
#     count += 1

# print(f"final count {count}")

max = ls[0]
min =ls[0]
for i in range(len(ls)):
    if ls[i] > max:
        max = ls[i]
    elif ls[i] < min:
        min = ls[i]

print(f"Max: {max}")
print(f"Min: {min}")
    





































































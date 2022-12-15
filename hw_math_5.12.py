from os import system
system('cls')

data = [1, 2, 3, 4, 5, 6, 7]

print("⬜ Source data:\n", data)
print()

# 1. set 0 to all the cells in the right half
Rhalf_idx = round(len(data)/2)         # round - округление
for i in range(Rhalf_idx, len(data)):
    data[i] = 0
print("🟠 Example 1:\n", data)
print()

# 2. (HW) set input value to all the cells in the left half
number = int(input("Number: "))
Lhalf_idx = len(data) - Rhalf_idx
for ii in range(0, Lhalf_idx + 1):
    data[ii] = number
print("✅ HW 1:\n", data)
print()

# 3. swap two values from idx 2 and 5
data = [1, 2, 3, 4, 5, 6, 7]
free = data[2]
data[2] = data[5]
data[5] = free
print("🟠 Example 2:\n", data)
print()

# 4.(HW) swap a pair 2,3 with 4,5
data = [1, 2, 3, 4, 5, 6, 7]
free = data[2]
free_1 = data[3]
data[2], data[3] = data[4], data[5]
data[4], data[5] = free, free_1
print("✅ HW 2:\n", data)
print()

# 5.(HW) swap left and right halfs of the list respecting the order
data = [1, 2, 3, 4, 5, 6, 7]
free = data[0:4]
free_2 = data[4:7]
data = free_2 + free
print("✅ HW 3:\n", data)
print()

# One more way :print("✅ HW 3:\n", data[4:7] + data[0:4])

# 6. calculate the sum and put it at the end
data = [1, 2, 3, 4, 5, 6, 7]
data.append(sum(data))
print("🟠 Example 3:\n", data)
print()

# 7. (HW) calculate the sum and put it at the start
data = [1, 2, 3, 4, 5, 6, 7]
data.insert(0, sum(data))            # insert добавляет туда, куда указывает индекс (первая цифра в скобке)
print("✅ HW 3:\n", data)

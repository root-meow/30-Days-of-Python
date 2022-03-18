#Using underscore as a var name
person = ("Bob", 42, "Mechanic")
name, _, profession = person

print(name, profession)
print()

for _ in range(10):
	print("Jameson")

for _ in range(10):
    print ("Test")

#Isolation of values
head, *tail = [1, 2, 3, 4, 5]

print(head)  # 1
print(tail)  # [2, 3, 4, 5]
print()

*head, tail = [1, 2, 3, 4, 5]

print(head)  # [1, 2, 3, 4]
print(tail)  # 5
print()

head, *middle, tail = [1, 2, 3, 4, 5]

print(head)    # 1
print(middle)  # [2, 3, 4]
print(tail)    # 5
print()

first, second, third, *rest = [1, 2, 3, 4, 5]
print(first)    # 1
print(second)  # [2, 3, 4]
print(third)
print(*rest)

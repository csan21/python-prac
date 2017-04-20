# for loop
# range() interates through sequence of numbers
# len() iterates through sequence using index
hobbies = ['basketball', 'gaming', 'coding', 'fishing']

for i in range(len(hobbies)):
    print("I like", hobbies[i])

# OUTPUT
# I like basketball
# I like gaming
# I like coding
# I like fishing


# for loop with else
numbers = [1, 2, 3, 4, 5, 4, 3, 2, 1]

for i in numbers:
    print(i)
else:
    print("Complete")

# OUTPUT
# 1
# 2
# 3
# 4
# 5
# 4
# 3
# 2
# 1
# Complete

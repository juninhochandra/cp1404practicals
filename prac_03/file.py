# Question 1
# Take the user's input and create a txt file with their name inside.
name = input("Enter your name: ")
out_file = open(name + ".txt", 'w')
out_file.write(name)
out_file.close()


# Question 2
# Read the txt file, take the name inside and say hi.
out_file = open(name + ".txt", 'r')
name = out_file.read()
out_file.close()
print(f"Hi {name}!")

# Question 3
# Read numbers.txt and print the sum of the first 2 numbers.
with open("numbers.txt", 'r') as out_file:
    num1 = out_file.readline()
    num2 = out_file.readline()
    print(int(num1) + int(num2))

# Question 4
# Read numbers.txt and print the total sum of every number on each line.
with open("numbers.txt", 'r') as file:
    total = 0
    for line in file:
        total += int(line)
    print(total)
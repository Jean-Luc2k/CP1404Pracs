out_file = open("name.txt", 'r+')
name = input("Please enter your name: ")
print(name, file=out_file)
out_file.close()

name_file = open("name.txt", 'r+')
name = name_file.read().strip()
name_file.close()
print("Your name is {}".format(name))

number_file = open("numbers.txt", 'r')
first_number = int(number_file.readline())
second_number = int(number_file.readline())
total = first_number + second_number
print(total)
number_file.close()

number_file = open("numbers.txt", 'r')
total = 0
for line in number_file:
    number = int(line)
    total = total + number
print(total)
number_file.close()

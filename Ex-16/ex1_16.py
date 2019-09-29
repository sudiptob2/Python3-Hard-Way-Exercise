from sys import argv

script,filename = argv

print(f"We are going to erase {filename}.")
print("If you don't want, hit CRTL-C (^C).")
print("If you do want that, hit RETURN.")

input("? ")

print(f"Opening the file {filename} ....")
target = open(filename,'w')
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I am going to write these to the file.")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print("Finally closing the file.")
target.close()

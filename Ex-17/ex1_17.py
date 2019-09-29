from sys import argv
from os.path import exists

script, from_file, to_file = argv

#Give a message of copying the contesnts of first file to the 2nd file
print(f"Copying from {from_file} to {to_file}")
indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long")
print(f"Does the output file exist?{exists(to_file)} ")
print("Ready, hit RETURN to continue, CRTL-C to abort.")
input()
out_file = open(to_file,'w')
out_file.write(indata)

print("Alright, all done")

out_file.close()

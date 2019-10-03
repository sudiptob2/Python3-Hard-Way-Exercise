import sys
#Takes 3 command line arguments
script, input_encoding, error = sys.argv

# A function
def main(language_file, encoding, errors):
    # Reaging the current line of the function and store it in a variable called line
    line = language_file.readline()

    if line: #if the variable contains some content then
        #print the content
        print_line(line, encoding, errors)
        # This is called recusion
        # Here the main function is called inside the main function again
        # This will work like an infinite loop
        # But if the line don't have any content the if statement will not execute
        # In that case the loop will break
        # So in each call to the main itself it will print the next print_line
        # And when there is no next line the function will finish execution
        return main(language_file,encoding, errors)

def print_line(line,encoding, errors):
    next_lang = line.strip() # Default is '\n' so this line strips depending on the newline character
    # Now to get raw byte we need to encode the characters using the encoding prvided in the command line
    raw_bytes = next_lang.encode(encoding, errors = errors)
    # We also want to show the main string (actual character view)
    # So we need to decode the raw_bytes
    # Or we could just print the line
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<===>", cooked_string)
    # print(raw_bytes, "<===>", line)


# This is the main portion of the program
# File is oppend from the local directory
language_file = open("languages.txt", encoding = "utf-8")
# Function we defined is called with the approriate parameter
main(language_file,input_encoding,error)

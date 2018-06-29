
input_file = open("input_file.txt","r")
text_on_file = input_file.readlines()
output_file = open("output_file.txt","w")
text_to_output = text_on_file[::-1]

for line in text_to_output:
    if line[-1] != '\n':
        output_file.write(line+'\n')
    else:
        output_file.write(line)
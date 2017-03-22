from variable_replace import *

file_input = open('input.txt', 'r')
file_output = open('output.txt', 'w')

text = file_input.read()
info = get_variables_info(text)
result = permutatio(text, info)
file_output.write(result)

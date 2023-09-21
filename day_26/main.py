
def get_numbers(file_name):
  with open(file_name, 'r') as file:
      lines = [line.rstrip() for line in file]
      return lines


file_1_list = get_numbers("/Users/dariabondarchuk/programming projects/python/bootcamp/python_bootcamp/day_26/file1.txt")
file_2_list = get_numbers("/Users/dariabondarchuk/programming projects/python/bootcamp/python_bootcamp/day_26/file2.txt")

print(file_1_list)
print(file_2_list)

output = [item for item in file_1_list if item in file_2_list]
print(output)

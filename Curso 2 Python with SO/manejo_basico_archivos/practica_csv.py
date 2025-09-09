import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""
  
  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename, "r") as archivo_csv:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(archivo_csv)
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string


#Call the function
#print(contents_of_file("flowers.csv"))


import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  f = open(filename)
    # Read the rows of the file
  rows = csv.reader(f)
    # Process each row
  for row in rows:
    if rows.line_num != 1:
      name, color, Type = row
      # Format the return string for data rows only

      return_string += "a {} {} is {}\n".format(name,color,Type)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))
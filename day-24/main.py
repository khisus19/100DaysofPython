with open("./my_file.txt", "a") as file:

    file.write("\nThis text was added")

with open("my_other_file.txt", "w") as other_file:
    other_file.write("This is my second file")
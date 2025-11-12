data = input("Enter something to write in the file: ")

with open("output.txt", "w") as file:
    file.write(data + "\n")

extra = input("Enter something more to append: ")

with open("output.txt", "a") as file:
    file.write(extra + "\n")

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())

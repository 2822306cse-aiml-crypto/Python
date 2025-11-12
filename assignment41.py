try:
    with open("sample.txt", "r") as file:
        lines = [line.strip() for line in file]
        
        for line in sorted(lines):
            print(line)
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")

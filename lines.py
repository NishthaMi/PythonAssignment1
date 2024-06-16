def read_lines_until_empty():
    lines = []
    
    while True:
        line = input("Enter a line (leave empty to finish): ")
        if line == "":
            break
        lines.append(line)
    
    print("\nYou entered:")
    for line in lines:
        print(line)

        read_lines_until_empty()
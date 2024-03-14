def draw_board(rows, columns):
    for i in range(rows):
        # Print horizontal line
        print(" ---" * columns)

        # Print vertical lines
        print("|   " * (columns + 1))

    # Print the last horizontal line
    print(" ---" * columns)

    return True


# Example usage
rows = int(input("Enter the number of rows: ")) #converting string to int
columns = int(input("Enter the number of columns: ")) #converting string to int

if draw_board(rows, columns):
    print("Board drawn successfully!")
else:
    print("Error drawing the board.")
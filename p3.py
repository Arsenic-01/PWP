class Operation:
    # Method with (int, char) sequence
    def operate(self, *args):
        if len(args) == 2:
            # Check if the first argument is an int and second is a char
            if isinstance(args[0], int) and isinstance(args[1], str) and len(args[1]) == 1:
                print(f"Integer: {args[0]}, Character: {args[1]}")
            # Check if the first argument is a char and second is an int
            elif isinstance(args[0], str) and len(args[0]) == 1 and isinstance(args[1], int):
                print(f"Character: {args[0]}, Integer: {args[1]}")
            else:
                print("Invalid arguments provided!")
        else:
            print("Please provide exactly two arguments.")

# Create object
op = Operation()

# First method call (int, char)
op.operate(5, 'A')

# Second method call (char, int)
op.operate('B', 10)

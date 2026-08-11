def py_calculator():
    """CLI calculator for multiple operations"""
    while True:
        # Choose an operation
        print("\n Python Calculator")
        print("\nAvailable operations: add, sub, mult, div, quit" )
        operation = input("Enter operation: ").strip().lower()

        #Check the break exit
        match operation:
            case "quit" :
                print("Exiting the program. Goodbye!")
                break

            case "add" | "sub" | "mult" | "div":
                #Get number only if valid math operation
                try:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                except ValueError:
                    print("Error: Please enter valid numeric values. ")
                    continue

                match operation:
                    case "add":
                        print(f"Result: {num1} + {num2} = {num1 + num2}")
                        
                    case "sub":
                        print(f"Result: {num1} - {num2} = {num1 - num2}")
                        
                    case "mult":
                        print(f"Result: {num1} * {num2} = {num1 * num2}")
                        
                    case "div":
                        if num2 == 0:
                            print("Error: cannot divide by zero")
                        else:
                            print(f"Result: {num1} / {num2} = {num1 / num2}")
                            
                        
            case _:
                print("Invalid operation! Please try add, sub, mult, div, or quit")
if __name__ == "__main__":
    py_calculator()
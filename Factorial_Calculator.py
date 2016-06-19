# Written by Spencer Lask with help from Kellen Lask, 5/21/2016; this program will output the factorial of any number


def calculate_factorial():
    try:    # Catch int parse errors
        # Receive integer input
        var = int(input("input number:"))
        var = abs(var)

        # Define the initial state
        iterations = 1
        running_product = 1

        # Iteratively counting to input + 1
        while iterations != var + 1:
            # Calculating running product by multiplying running product by the current iteration
            running_product = running_product * iterations
            iterations = iterations + 1

        # Print output
        print(running_product)

    # Communicate invalidity of input
    except:
        print("Input an integer")
        calculate_factorial()

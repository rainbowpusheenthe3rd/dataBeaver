from metabeaver.Formatting.printControl import PrintControl, conditional_print as cprint


# Usage example:
def yesPrint():
    # Your code using conditional_print here
    global print_control
    cprint('Inside yesPrint!')
    # Rest of your code

def noPrint():
    # Your code using conditional_print here
    cprint('Inside noPrint!')
    # Rest of your code


# Initialize the global print_control to enabled=False to disable printing by default
print_control = PrintControl(enabled=True)  # Change to False if you want to disable printing globally
yesPrint()

print_control = PrintControl(enabled=False)  # Change to False if you want to disable printing globally
noPrint()
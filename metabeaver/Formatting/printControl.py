# Import the printControl manager
from metabeaver.Formatting.printControl import enable_print

class PrintControl:
    def __init__(self, enabled=True):
        self.enabled = enabled
        self.original_enabled = enabled

    def __enter__(self):
        self.original_enabled = self.enabled
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.enabled = self.original_enabled

def conditional_print(message):
    # Use the global print_control
    global print_control
    if print_control and print_control.enabled:
        print(message)

# Usage example:
def yesPrint():
    # Your code using conditional_print here
    conditional_print('Inside yesPrint!')
    # Rest of your code

def noPrint():
    # Your code using conditional_print here
    conditional_print('Inside noPrint!')
    # Rest of your code



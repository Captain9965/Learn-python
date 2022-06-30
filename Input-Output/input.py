"""
The input() function is used
"""

def get_input():
    input_ = input("Enter your age: ")
    print(type(input_))
    return input_
def Main():
    print("----With input():-----")
    result = get_input()
    print(result)
if __name__ == "__main__":
    Main()
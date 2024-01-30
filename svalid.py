#string validation
if __name__ == '__main__':
    s = input()
    
    # Check if the string contains alphanumeric characters
    print(any(char.isalnum() for char in s))
    
    # Check if the string contains alphabetical characters
    print(any(char.isalpha() for char in s))
    
    # Check if the string contains digits
    print(any(char.isdigit() for char in s))
    
    # Check if the string contains lowercase characters
    print(any(char.islower() for char in s))
    
    # Check if the string contains uppercase characters
    print(any(char.isupper() for char in s))

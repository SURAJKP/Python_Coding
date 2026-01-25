str = ['h', 'e', 'l', 'l', 'o'];
output = [];

def reverseString(s):
    for i in range(len(s)-1, -1, -1):
        output.append(s[i])
    return output

# Example usage:
result = reverseString(str)
print(result)  # Output: ['o', 'l', 'l', 'e', 'h']

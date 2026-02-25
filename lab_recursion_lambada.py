# 1) Recursive function to count vowels (case insensitive)
def count_vowels_recursive(text, index=0):
    vowels = "aeiouAEIOU"
    
    # Base case: end of string
    if index == len(text):
        return 0
    
    # Count 1 if current character is a vowel, else 0
    count = 1 if text[index] in vowels else 0
    
    # Recursive call
    return count + count_vowels_recursive(text, index + 1)


# 2) Using map() with lambda to create a new list of squared numbers
numbers = [40, 35, 10, 15, 20]

squared_list = list(map(lambda x: x * x, numbers))

print(squared_list)
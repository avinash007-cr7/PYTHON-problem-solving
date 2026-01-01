# taking input from the user
input_string = input("Enter a string: ")

if input_string:
    result=input_string[0]    #storing the first character default and it is used for comparing
else:
    result=""
# Loop start from 2nd character
for i in range(1, len(input_string)):
    # comparison
    if input_string[i] != input_string[i - 1]:
        result += input_string[i]
output = (result, len(result))

# Print result
print("the string without duplicates:",output)

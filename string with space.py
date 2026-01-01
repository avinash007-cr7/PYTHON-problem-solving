string_input = input("Enter a string: ")

max_len = 0      # stores maximum length found
current_len = 0  # stores current substring length

# Traverse each character
for ch in string_input:
    if ch != " ":
        current_len += 1        # extend current substring
        if current_len > max_len:
            max_len = current_len
    else:
        current_len = 0         # reset when space found

print(max_len)

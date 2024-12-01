def all_substrings(s):
  """
  Generates all substrings of a given string.

  Args:
    s: The input string.

  Returns:
    A list of all substrings of the string.
  """

  substrings = []
  for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
      substrings.append(s[i:j])
  return substrings

# Get input from the user
string = input("Enter a string: ")

# Find all substrings
substrings_list = all_substrings(string)

# Print the substrings
print("All substrings of the string are:")
for substring in substrings_list:
  print(substring)
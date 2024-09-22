#adding a tab
print("python")
print("\tpython")

# newline string
print("langauges:\nPython\nc\nJavascript")

# Combine tabs and newlines
print("langauges:\n\tPython\n\tC\n\tJavascript")

# Stripping whitespace - extra whitespace can be confusing, can be used to elimate whitespace from data people enter
favorite_language = 'python '
favorite_language = favorite_language.rstrip() # associate stripped value to variable
print(favorite_language)
print(favorite_language.rstrip()) # temp removes whitespace from right side, but calling favorite_language again will bring it back
print(favorite_language.lstrip()) # removes white space from left side
print(favorite_language.strip()) # removes white space from both sides



#methods - an action that python can perform on a piece of data
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#f-strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" #f-strings - f is for format, pythong formats the string by replacing the name of any variable in braces with it's value
print(full_name.title())
print(f"Hello, {full_name.title()}!")

#f-strings to compose a message
message = f"Hello, {full_name.title()}"
print(message)

user_name = "Tom"
print(f"Hi {user_name}, would you like to learn python?")

author = "albert einstein"
qoute = 'A person who never made a mistake never tried anything new'
print(f'{author} once said, "{qoute}"')

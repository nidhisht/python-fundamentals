message1 = "Hello World!"

print(message1.upper()) # output: HELLO WORLD!
print(message1.lower()) # output: hello world!


message2 = "HELLO"
print(message2.isupper())   # output: True
print(message2.islower())   # output: False


print("this is a string".startswith("this")) # output: True
print("this is a string".startswith("This")) # output: False


print("this is a string".endswith("string")) # output: True
print("this is a string".endswith("g")) # output: True
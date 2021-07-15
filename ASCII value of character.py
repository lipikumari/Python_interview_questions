#Find the ASCII value of a character
#The machine doesn’t have the capacity to understand languages that humans do, the machine understands binary language
#and converts everything to binary format. According to The American Standard Code for Information Interchange[ASCII] every number,
#character or any special symbol has a unique value and are ranging from 0 to 127
#0 t0 31 and 127:- End of File/Stream
#32 to 126:- Printable Characters
#Characters ranging from 32 to 126 includes uppercase
#alphabets, lowercase alphabets, numeric digit from 0-9 and all special characters

#Note- ord() a predefined function is used to get ASCII value
Char=input("Enter the character:")
ASCIIval=ord(Char)
print(ASCIIval)

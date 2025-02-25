text1="Monty"
text2="Python's"
text3="Flying Circus"

print(len("Monty"))
print(len("Python's"))
print(len("Flying Circus"))

text1 = ' '*(40-(len("Monty")))+"Monty"
text2 = ' '*(40-(len("Python's")))+"Python's"
text3 = ' '*(40-(len("Flying Circus")))+"Flying Circus"

print(text1)
print(text2)
print(text3)
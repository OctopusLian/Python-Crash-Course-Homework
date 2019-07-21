prompt = "\nTell me Pizza Toppings"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = raw_input(prompt)

    if message == 'quit':
        active = False
    else:
        print('add ' + message)
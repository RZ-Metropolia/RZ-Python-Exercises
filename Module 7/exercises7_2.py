prompt = "\nPlease enter your name: "
prompt += "\n(Press 'enter' button to quit)\n"
names = []
existing_names = {'eric', 'ana', 'tim', 'lee', }

while True:
    name = input(prompt)

    if name == '':
        break
    else:
        names.append(name.lower())

    for name in names:
        if name.lower() in existing_names:
            print(f"{name.title()}: Existing name")
        else:
            print(f"{name.title()}: New name")
            existing_names.add(name.lower())

print(f"The set of existing names: {existing_names}")

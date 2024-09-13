prompt = "Please enter your name: "
prompt += "(Press 'enter' button to quit)\n"
names = []
existing_names = {'eric', 'ana', 'tim', 'lee', }

while True:
    name = input(prompt)

    if name == '':
        break
    else:
        names.append(name.lower())

names_set = set(names)

if len(names_set) == 0:
    print("You did not enter a name.")
else:
    for name in names_set:
        if name in existing_names:
            print(f"{name.title()}: Existing name")
        else:
            print(f"{name.title()}: New name")
            existing_names.add(name)
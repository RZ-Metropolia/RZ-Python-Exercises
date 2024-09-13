prompt = "\nHow may I help you?\n"
prompt += "Input '1' to enter information of a new airport.\n"
prompt += "Input '2' to fetch the information of an existing airport.\n"
prompt += "Input 'q' to quit.\n"

airport_info = {
    'EFHK': 'Helsinki-Vantaa Airport',
    'EFHF': 'Helsinki-Malmi Airport',
    'RJTT': 'Tokyo International Airport',
    }

user_input = input(prompt)
while user_input != 'q':
    if user_input == '1':
        icao_code = input("Please enter the ICAO code of the airport: ")
        if icao_code.upper() in airport_info.keys():
            print(f"We already have information for ICAO code '{icao_code}'.")
            print(f"ICAO code '{icao_code.upper()}' is '{airport_info[icao_code.upper()]}'")
        else:
            airport_name = input("Please enter the name of the airport: ")
            airport_info[icao_code.upper()] = airport_name.title()
            print("The information has been saved.")

        user_input = input(prompt)
    elif user_input == '2':
        icao_code = input("Please enter the ICAO code of the airport: ")
        if icao_code.upper() not in airport_info.keys():
            print(f"We don't have information for the ICAO code '{icao_code}'")
        else:
            print(f"ICAO code '{icao_code.upper()}' is '{airport_info[icao_code.upper()]}'")

        user_input = input(prompt)

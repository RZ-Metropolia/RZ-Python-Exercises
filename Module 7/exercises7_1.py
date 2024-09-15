winter_months = (12, 1, 2)
spring_months = (3, 4, 5)
summer_months = (6, 7, 8)
autumn_months = (9, 10, 11)

seasons = ('winter', 'spring', 'summer', 'autumn')

season_number = int(input("Please enter the number of the month: "))

if season_number in winter_months:
    print(f"The season is {seasons[0]}")
elif season_number in spring_months:
    print(f"The season is {seasons[1]}")
elif season_number in summer_months:
    print(f"The season is {seasons[2]}")
elif season_number in autumn_months:
    print(f"The season is {seasons[3]}")

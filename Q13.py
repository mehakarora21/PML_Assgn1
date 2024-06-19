from datetime import date
year=int(input("Input enter birth year: "))
current_date=date.today()
current_year=current_date.year
age=current_year-year
print("Your age by the E.O.Y: ", age)

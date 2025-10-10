import calendar

year=int(input("Enter year: "))
mon_th=int(input("Enter month: "))

calendar=calendar.month(year, mon_th) # month function
print(calendar)


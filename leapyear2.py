year1=int(input("Enter starting year:"))
year2=int(input("Enter final year:"))
print(f"Leap years from{year1}to {year2}:")
for year in range(year1,year2 +1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year)

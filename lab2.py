number_of_years=int(input("Enter the number of years :"))
print(f"for year {number_of_years}: ")
total=0
for month in range(1,13):
   enter_rainfall=int(input(f"Enter the rainfall for month {month} : "))
   total+=enter_rainfall
print("For 12 months")
print(f"Total rainfall: {total} centimetreers")
print(f"Average rainfall: {total/(number_of_years*12)} centimetreers")
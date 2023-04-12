starting_count = float(input("Enter the starting count of organisms: "))
daily_increase = float(input("Enter the average daily increase as a percentage: "))
num_days = int(input("Enter the number of days to multiply: "))

if starting_count < 0 or daily_increase < 0 or num_days < 0:
    print("Please enter positive values only.")
else:
    daily_increase = daily_increase / 100 + 1  
    print(f"Starting count: {starting_count}")
print("Day Approximate")
print("---------------------------------")

for day in range(num_days):
       
        print(f"Day {day+1}: {starting_count:.2f}")
        starting_count *= daily_increase
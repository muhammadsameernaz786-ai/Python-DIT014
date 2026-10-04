name = input("enter your name : ").upper()
total = 0
days_above_target = 0
for day in range(1, 8):
    hours = int(input(f"Day {day} : "))
    total = total + hours
    if hours > 2:
        days_above_target = days_above_target + 1

average = total / 7
if average < 1:
    performance = "low"
elif 1 < average < 2:
    performance = "medium"
elif average > 2:
    performance = "high"

print("STUDYSPARK WEEK REVIEW\n")

print(f"Student :        {name}")
print(f"Total Hours :     {total}")
print(f"Average :          {average:.2f}")
print(f"Days above target :       {days_above_target}")
print(f"Performance :              {performance}")
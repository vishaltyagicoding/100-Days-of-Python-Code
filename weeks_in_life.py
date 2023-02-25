age = int(input("Enter your current age? "))

# 90 years

# 1 years 365 or 12 months 52 weeks

years_remaining = 90 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and " \
          f"{years_remaining} years left."

print(message)

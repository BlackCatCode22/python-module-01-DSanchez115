# David Sanchez
# CIT-95-30164-2024FA
# PythonFall24Module01
# 3. gross_pay.py This program will prompt the user for weekly hours worked and their hourly rate,
# then will compute and output gross pay. Bonus if you can handle overtime
# (hours worked over 40 hours will be paid at time and a half)


weekly_hours = float(input("How many hours did you work this week ?"))
hour_rate = float(input("How much do you make per hour ?"))

gross_pay = weekly_hours * hour_rate

print("Your grossed $" + str(gross_pay), "this week.")



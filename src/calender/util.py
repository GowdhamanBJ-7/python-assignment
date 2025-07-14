import calendar


def day_finder(input_date):
        # mm dd yyyy
        day_of_week = calendar.weekday(int(input_date[2]), int(input_date[0]), int(input_date[1]))

        day_name = calendar.day_name[day_of_week]
        return day_name.upper()


'''
# import calendar
#
# print(calendar.TextCalendar(firstweekday=6).formatyear(2025))
#
# print(calendar.month(2000,7))
#
#
#
# # Input: day, month, year
# day = 8
# month = 5
# year = 2025
#
# # Find the day of the week (0=Monday, 6=Sunday)
# day_of_week = calendar.weekday(year, month, day)
# print(day_of_week)
# # Map the day index to the day name
# day_name = calendar.day_name[day_of_week]
#
# print(f"The date {day}/{month}/{year} falls on a {day_name}.")

'''

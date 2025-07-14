from src.calender.util import day_finder

date_month_year = input()
input_date = date_month_year.split(' ')
print(input_date)
day = day_finder(input_date)
print(day)

'''
mm dd yyyy

Sample Input
08 05 2015

Sample Output
WEDNESDAY
'''
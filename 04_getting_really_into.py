# 1. You slept for 6.2, 7, 8, 5, 6.5, 7.1, and 8.5 hours this week.
#  Calculate the average number of hours slept.
#
# sleep_per_day = list()
# sleep_per_day.append(6.2)
# sleep_per_day.append(7)
# sleep_per_day.append(8)
# sleep_per_day.append(5)
# sleep_per_day.append(6.5)
# sleep_per_day.append(7.1)
# sleep_per_day.append(8.5)
#
# print(f"There are {len(sleep_per_day)} sleeping nights")
#
# # for idx, day in enumerate(sleep_per_day):
# #     print(f"{idx} - {day}")
# # 1 day sleep = 6.2
#
#
# sum_of_sleep = 0
# for day in sleep_per_day:
#     sum_of_sleep += day
#
#
# # sum_of_sleep = [ sum(day) for day in sleep_per_day ]
#
# # 1. Znalezc gotowa biblioteke, np. numpy/pandas
# # 2. Lambda
# # 3. Dict/List comprehension
#
# print(f"Average sleep time is: {(sum_of_sleep / len(sleep_per_day)):.2f}")

# 4. Wikipedia defines leap years as:
# Every year that is:
#   exactly divisible by four is a leap year,
#       except for years that  are exactly divisible by 100,
#           except but these centurial years are leap years if they are exactly divisible by 400.
#
# For example, the years 1700, 1800, and 1900 are
# not leap years, but the years 1600 and 2000 are.
# https://en.wikipedia.org/wiki/Leap_year
# Write Python code to determine if 1800, 1900, 1903, 2000, and 2002 are leap years.

def is_leap_year(year: int) -> bool:

    if not year % 400:
        return True
    if not year % 4 and year % 100:
        return True

    return False


print(is_leap_year(year=1600))

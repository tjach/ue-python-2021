# 1. You slept for 6.2, 7, 8, 5, 6.5, 7.1, and 8.5 hours this week.
#  Calculate the average number of hours slept.
# Remarks: https://www.geeksforgeeks.org/find-average-list-python/


# 4. Wikipedia defines leap years as:
# Every year that is exactly divisible by four is a leap year, except for years that
# are exactly divisible by 100, but these centurial years are leap years if they
# are exactly divisible by 400. For example, the years 1700, 1800, and 1900 are
# not leap years, but the years 1600 and 2000 are.
# https://en.wikipedia.org/wiki/Leap_year
# Write Python code to determine if 1800, 1900, 1903, 2000, and 2002 are leap years.
from statistics import mean

sleep_per_night = [6.2, 7, 8, 5, 6.5, 7.1, 8.5]

# sum = 0
#
# for night in sleep_per_night:
#     sum += night
# else:
#     result = sum / len(sleep_per_night)
#
# print(result)


print(mean(sleep_per_night))











# avg = 0
# for night in sleep:
#     avg += night
# avg /= len(sleep)
#
# print(avg)

# avg = sum(sleep) / len(sleep)
# print(avg)

# avg = reduce(lambda e1, e2: e1 + e2, sleep) / len(sleep)
# print(avg)

# avg = mean(sleep)
# print(avg)
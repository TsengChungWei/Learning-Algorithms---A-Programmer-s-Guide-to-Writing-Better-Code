# Listing 3-1. Code to print readable calendar for any month and year


from datetime import date
import calendar

def print_month(month, year):
    idx = key_array.index(month)                # 1
    day = 1

    wd = date(year,idx + 1,day).weekday()       # 2
    wd = (wd + 1) % 7                           # 3
    end = month_length[idx]                     # 4
    if calendar.isleap(year) and idx == 1:      # 5
        end += 1

    print('{} {}'.format(month,year).center(20))
    print('Su Mo Tu We Th Fr Sa')
    print('   ' * wd, end='')                   # 6
    while day <= end:
        print('{:2d} '.format(day), end='')
        wd = (wd + 1) % 7                       # 7
        day += 1
        if wd == 0: print()                     # 8
    print()

month_length = [31, 28, 3, 30, 31, 30, 31, 31, 30, 31, 30, 31]

key_array   = [ 
    'January',  'February', 'March',    'April',    'May',      'June', 
    'July',     'August',   'September','October',  'November', 'December' 
]

# 1. Find index to use for month_length, an integer from 0 to 11.
# 2. Returns weekday for first day of given month, using 0 for Monday. Note date()
#    uses idx + 1 since its month argument must be an integer from 1 to 12.
# 3. Adjust to have Sunday be the weekday with a value of 0, instead of Monday.
# 4. Determine length of the month corresponding to input parameter.
# 5. In a leap year, February (index 1 when counting from 0) has 29 days.
# 6. Add spaces in first week to start day 1 at right indentation.
# 7. Advance day and weekday for next day.
# 8. Insert line break before Sunday to start a new line.


days_in_month = { 
    'January'  :31, 'February':28, 'March'   :31, 'April'   :30,
    'May'      :31, 'June'    :30, 'July'    :31, 'August'  :31,
    'September':30, 'October' :31, 'November':30, 'December':31 
}


month = "February"
year = 2024
print_month(month, year)
print()
print('April has', days_in_month['April'], 'days')

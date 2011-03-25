
century_key = { 1900 : 0, 2000 : 6 }
month_key = [ 0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5 ]
leap_month_key = [ 6, 2, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5 ]

def initial_sundays_in_year(year):
    # See http://en.wikipedia.org/wiki/Calculating_the_day_of_the_week
    y = year % 100
    c_value = century_key[(year / 100) * 100]
    m_keys = leap_month_key if y % 4 == 0 else month_key
    return sum([1 for key in m_keys if (c_value + y + y/4 + key + 1) % 7 == 0])


def euler19():
    """How many Sundays fell on the first of the month during the twentieth
    century?"""
    sundays = sum([initial_sundays_in_year(y) for y in range(1901, 2001)])
    print "%d Sundays fell on the first in the 20th century" % sundays
    return sundays


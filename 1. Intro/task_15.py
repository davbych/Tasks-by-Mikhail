days_in_month = {"January": 31, "February": 28,
                      "March": 31, "April": 30,
                      "May": 31, "June": 30,
                      "July": 31, "August": 31,
                      "September": 30, "October": 31,
                      "November": 30, "December": 31}
def visoc_year(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)
def days_in_month(year, month):
    if visoc_year(year) and month == "February":
        return 28
    try:
        return days_in_month[month]
    except KeyError:

        return None

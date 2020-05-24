def getStartEndOfMonth(date):
# Returns first and last day of a month, taking a datetime.datetime object as an argument

        firstDate = date.replace(day=1)

        if date.month != 12:
            lastDate = datetime.datetime(date.year, date.month + 1, 1) - datetime.timedelta(days=1)
        else:
            lastDate = datetime.datetime(date.year + 1, 1, 1) - datetime.timedelta(days=1)

        dates = (firstDate, lastDate)
        return (dates)

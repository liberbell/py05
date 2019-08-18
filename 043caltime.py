from datetime import datetime, timedelta
import calendar

now = datetime.now()

testData = now + timedelta(days=2)
myFirstcorse = now - timedelta(weeks=3)
print(testData.date())
print(myFirstcorse.date())

if testData > myFirstcorse:
    print('Comparison works')

cal = calendar.month(2019, 6)
print(cal)

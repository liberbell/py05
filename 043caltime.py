from datetime import datetime, timedelta

now = datetime.now()

testData = now + timedelta(days=2)
myFirstcorse = now - timedelta(weeks=3)
print(testData.date())
print(myFirstcorse.date())

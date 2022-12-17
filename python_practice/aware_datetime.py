import datetime

d = datetime.date(2022,12,12)
d1 = datetime.datetime(2022,12,12,hour=15,minute=0,tzinfo=datetime.timezone.utc)


print(d1.tzinfo)
print(d.day)

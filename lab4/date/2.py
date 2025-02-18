import datetime as dat
print(f"To day is: {dat.datetime.now()}")
print(f"tomorow {dat.datetime.now() + dat.timedelta(days=1)}")
print(f"yesterday: {dat.datetime.now() - dat.timedelta(days=1)}")
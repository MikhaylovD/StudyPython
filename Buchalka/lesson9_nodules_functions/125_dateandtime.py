import time

print("the epoch start " + time.strftime('%c', time.gmtime(0)))

print("current time {0} with offset {1} ".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("\t daylight saving time is in effect for thi location")
    print("\t dst timezone is " + time.tzname[1])

print("local time is " + time.strftime('%Y-%m-%d %H:%M:S', time.localtime()))
print("utc time is " + time.strftime('%Y-%m-%d %H:%M:S', time.gmtime()))
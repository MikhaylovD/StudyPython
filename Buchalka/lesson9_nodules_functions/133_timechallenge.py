import datetime
import pytz

available_zones = {'1': "Africa/Tunis",
                   '2': "Asia/Koltaka",
                   '3': "Europe/Brussels",
                   '4': "Japan",
                   '5': "Zulu"}

print(" chose tz")
for place in sorted(available_zones):
    print("\t{}. {}".format(place, available_zones[place]))

while True:
    choice = input()

    if choice == '0':
        break

    if choice in available_zones.keys():
        tz_to_display = pytz.timezone(available_zones[choice])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {} {}".format(available_zones[choice], world_time.strftime('%A %x %X %z'), world_time.tzname()))
        print("local time is {}".format(datetime.datetime.now().strftime('%A %x %X %z')))
        print("local time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X %z')))
        print()
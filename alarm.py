from datetime import datetime
from playsound import playsound

alarm_time = input("Enter the time of alarm to be set (HH:MM:SS): ")
alarm_hour = int(alarm_time[0:2])
alarm_minute = int(alarm_time[3:5])
alarm_seconds = int(alarm_time[6:8])
alarm_period = alarm_time[9:11].upper()

print("Setting up the alarm...")

while True:
    now = datetime.now()
    current_hour = int(now.strftime("%I"))
    current_minute = int(now.strftime("%M"))
    current_seconds = int(now.strftime("%S"))
    current_period = now.strftime("%p").upper()

    if alarm_period == current_period and alarm_hour == current_hour and alarm_minute == current_minute and alarm_seconds == current_seconds:
        print("Wake Up!")
        playsound('audio.mp3')
        break
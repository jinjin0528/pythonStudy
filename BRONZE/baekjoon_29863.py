sleep_time = int(input())  # 수면 시작 시간
alarm_time = int(input())  # 알람 시간

if alarm_time >= sleep_time:
    sleep_duration = alarm_time - sleep_time
else:
    sleep_duration = (24 - sleep_time) + alarm_time

print(sleep_duration)

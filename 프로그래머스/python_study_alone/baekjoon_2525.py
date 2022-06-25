hour, minute = map(int,input().split())
time_to_cook = int(input())

hour = hour + (time_to_cook // 60)
minute = minute + (time_to_cook % 60)

if minute >= 60:
    hour = hour + 1
    minute = minute - 60
if hour >= 24:
    hour = hour - 24

print(hour,minute)
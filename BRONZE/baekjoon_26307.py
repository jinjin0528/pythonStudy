hh, mm = map(int,input().split())
start_hh, start_mm = 9, 0

time = (hh-start_hh)*60 + (mm+start_mm)
print(time)
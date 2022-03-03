t = int(input('enter time in sec:   '))
hour = t // 3600
min = t % 3600
sec = t % 60
# if t < 60:
#     print(f"time 00:00:{sec:02}")
# # elif t < 3600:
# #     print(f"time 00:{min:02}:{sec:02}")
# else:
print(f"time {hour:02}:{min//60:02}:{sec:02}")
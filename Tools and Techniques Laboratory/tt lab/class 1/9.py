# Take 2 times in 24hr hh:mm:ss format and add them
time1 = list(map(int, input("Enter time 1: ").split(':')))
time2 = list(map(int, input("Enter time 2: ").split(':')))
time = [0, 0, 0]
time[2] = time1[2] + time2[2]
time[1] = time1[1] + time2[1] + (time[2] // 60)
time[0] = time1[0] + time2[0] + (time[1] // 60)
time[2] %= 60
time[1] %= 60
time[0] %= 24
time = ['0' + str(time[0]) if time[0] < 10 else time[0],
        '0' + str(time[1]) if time[1] < 10 else time[1],
        '0' + str(time[2]) if time[2] < 10 else time[2]]
print(f"Sum of time: {time[0]}:{time[1]}:{time[2]}")
# login = [1, 2, 3,12,13,14]
# logout = [10, 8, 4,16,16,16]

login = [1, 2, 3]
logout = [10, 8, 4]

timeline = []
for num in login:
    timeline.append((num, True))

for num in logout:
    timeline.append((num, False))

timeline.sort()

print(timeline)

numUser = 0
maxUser = 0
maxDay = 0
currDay = 0
prevDay = 0

# hMap
# 1: 4
# 2: 4

for time in timeline:
    if time[1]: ## Girisler
        numUser += 1
        if numUser > maxUser:
            maxDay = 0
        maxUser = max(maxUser, numUser)

    if maxUser == numUser:
        maxDay += (time[0]-prevDay)

    if not time[1]: # Cikislar
        numUser -= 1

    prevDay = time[0]


print(maxDay)
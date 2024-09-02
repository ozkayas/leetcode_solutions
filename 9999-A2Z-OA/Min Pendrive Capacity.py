def fillDrives(arr, capacity) -> int:
    l, r = 0, len(arr) - 1
    filled = []
    while l <= r:
        if l == r:
            filled.append(arr[r])
            r -= 1
        elif arr[l] + arr[r] <= capacity:
            filled.append(arr[l] + arr[r])
            l += 1
            r -= 1
        elif arr[r] <= capacity:
            filled.append(arr[r])
            r -= 1

    print(filled)
    return len(filled)


def findMinimumPenDriveCapacity(gameSize, k) -> int:
    gameSize.sort()

    mn, mx = gameSize[-1], sum(gameSize[-2:])
    # print(mn,mx)
    # binary search between mn, mx
    l, r = mn, mx
    ans = mx
    while l <= r:
        pdc = l + (r - l) // 2

        if fillDrives(gameSize, pdc) <= k:
            # this drivesize is ok, but seems big, we can decrease it
            ans = pdc
            r = r - 1
        else:
            l = l + 1

    return ans


# print(fillDrives([2,3,4,4,6,9],9))
print(findMinimumPenDriveCapacity([2, 3, 5, 4, 6, 9, 9], 3))
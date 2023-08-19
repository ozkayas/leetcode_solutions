def compareVersion(version1: str, version2: str) -> int:
    v1 = version1.split(".")
    v2 = version2.split(".")

    maxLenght = max(len(v1), len(v2))

    for i in range(maxLenght):
        # add 0 for non existing
        if i == len(v1):
            v1.append("0")
        if i == len(v2):
            v2.append("0")
        if int(v1[i]) < int(v2[i]):
            return -1
        if int(v1[i]) > int(v2[i]):
            return 1

    return 0


compareVersion("1", "1.1")
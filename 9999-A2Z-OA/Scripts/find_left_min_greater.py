import bisect


# Her bir eleman için kendsinin solundaki tum elemanlar arasında kendisinden büyük olanlarin en küçüğünü bulma
def find_left_min_greater(arr):
    result = [-1] * len(arr)  # Sonuçları tutacak liste
    sorted_list = []  # Soldaki elemanları sıralı tutmak için boş liste

    for i in range(len(arr)):
        # arr[i]'den büyük olan ilk elemanı bulmak için binary search yapalım
        pos = bisect.bisect_right(sorted_list, arr[i])

        # Eğer pos sıfır değilse, kendisinden büyük en küçük elemanı bulduk
        if pos < len(sorted_list):
            result[i] = sorted_list[pos]

        # Şu anki elemanı sıralı bir şekilde listeye ekleyelim
        bisect.insort(sorted_list, arr[i])

    return result

print(find_left_min_greater([6,4,3,5,2,1]))  # [-1, 6, 4, 4, 3, 2]
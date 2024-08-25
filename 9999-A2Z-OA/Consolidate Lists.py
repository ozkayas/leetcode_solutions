'''Question:
Imagine you're interacting with Alexa. When you command Alexa to "acquire a certain item", it begins to retrieve information from a variety of sources, which we'll refer to as 'catalogues'. Each catalogue responds with a sorted list of potential matches. Your task is to write a program that can consolidate these sorted lists into one coherent list.

Example:

Prime: [2, 5, 8]
Whole Foods: [1, 3, 4]
Pantry: [7, 9]
Answer: [1, 2, 3, 4, 5, 7, 8, 9]
'''
import heapq
from typing import List

def mergeCatalogues(catalogues: List[List[int]]):
    min_heap = []
    result = []

    # Each entry in the heap is a tuple: (value, index of the catalogue, index of the element in the catalogue)
    for i, catalogue in enumerate(catalogues):
        if catalogue:
            heapq.heappush(min_heap, (catalogue[0], i, 0))

    while min_heap:
        value, i, j = heapq.heappop(min_heap)
        result.append(value)
        
        # If there's a next element in the same catalogue, push it onto the heap
        if j + 1 < len(catalogues[i]):
            heapq.heappush(min_heap, (catalogues[i][j + 1], i, j + 1))

    return result

# Örnek kullanım
prime = [2, 5, 8]
whole_foods = [1, 3, 4]
pantry = [7, 9]

print(mergeCatalogues([prime, whole_foods, pantry]))  # Çıktı: [1, 2, 3, 4, 5, 7, 8, 9]




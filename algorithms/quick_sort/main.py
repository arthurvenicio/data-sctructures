def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Exemplo de uso
arr = [3, 6, 8, 10, 1, 2, 1]
print(quicksort(arr))  # Saída: [1, 1, 2, 3, 6, 8, 10]


# Worst case is time complexy O(n²), and average case O(n log n)
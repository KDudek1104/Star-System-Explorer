def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x.distance < pivot.distance]
    middle = [x for x in arr if x.distance == pivot.distance]
    right = [x for x in arr if x.distance > pivot.distance]
    return quicksort(left) + middle + quicksort(right)

def sort_stars_by_distance(stars):
    return quicksort(stars)

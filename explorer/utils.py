# utils.py
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def sort_stars_by_distance(stars):
    distances = [star.distance for star in stars]
    sorted_distances = quicksort(distances)
    sorted_stars = [star for dist in sorted_distances for star in stars if star.distance == dist]
    return sorted_stars

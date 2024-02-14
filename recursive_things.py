def sum_arr(arr):
  if not arr:
    return 0
  
  return arr[0] + sum_arr(arr[1:])

def get_length(arr):
  if not arr:
    return 0
  
  return 1 + get_length(arr[1:])

def find_max(arr):
  if not arr:
    return 0
  elif len(arr) == 1:
    return arr[0]
  elif len(arr) == 2:
    return arr[0] if arr[0] > arr[1] else arr[1]
  
  sub_max = find_max(arr[1:])

  return arr[0] if arr[0] > sub_max else sub_max

def binary_search_recursive(arr, target):
  if not arr:
    return -1
  
  i, j = 0, len(arr) - 1
  mid = (i + j) // 2

  if arr[mid] == target:
    return mid
  elif arr[mid] < target:
    return binary_search_recursive(arr[mid + 1:], target)
  else:
    return binary_search_recursive(arr[:mid], target)

print(sum_arr([2, 4, 6]))
print(get_length([2, 4, 6, 5, 1]))
print(find_max([2, 7, 6, 5, 1]))
print(binary_search_recursive([1, 3, 5, 6, 8, 9], 5))

# KMP Substring Search

def get_arr_pattern(p):
  arr = [0]
  p_length = len(p)
  i, j = 1, 0

  while len(arr) < p_length:
    if p[j] != p[i] and j == 0:
      arr.append(0)
      i += 1
    elif p[j] != p[i]:
      j = arr[j - 1]
    else:
      arr.append(j + 1)
      i += 1
      j += 1
  
  return arr

def knuth_morris_pratt(t, p):
  arr = get_arr_pattern(p)
  t_length = len(t)
  p_length = len(p)
  i, j = 0, 0

  while i < t_length:
    if t[i] != p[j] and j == 0:
      i += 1
    elif t[i] != p[j]:
      j = arr[j - 1]
    else:
      i += 1
      j += 1

      if j == p_length:
        return i - p_length
    
  return -1


def test():
  # Test Temp Array Pattern
  assert get_arr_pattern("abcdabca") == [0, 0, 0, 0, 1, 2, 3, 1]
  assert get_arr_pattern("aabaabaaa") == [0, 1, 0, 1, 2, 3, 4, 5, 2]
  assert get_arr_pattern("acacabacacabacacac") == [0, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 4]
  
  # Test KMP Algorithm
  assert knuth_morris_pratt("abxabcabcaby", "abcaby") == 6
  assert knuth_morris_pratt("abcbcglx", "bcgl") == 3
  assert knuth_morris_pratt("aaaaaaab", "aaab") == 4


if __name__ == "__main__":
  test()
  print("Everything's OKAY")

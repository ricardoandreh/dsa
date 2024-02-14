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


# Test 1
text = "abxabcabcaby"
pattern = "abcaby"

# Test 2
# text = "abcbcglx"
# pattern = "bcgl"

print(knuth_morris_pratt(text, pattern))

# Test Array Pattern
# pattern = "abcdabca"
# pattern = "aabaabaaa"
# print(get_arr_pattern(pattern))

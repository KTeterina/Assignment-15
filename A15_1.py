def cut_rod(n, prices):
  # maximum value for each rod length
    max_value = [0] * (n + 1) 

  # cut lengths that lead to the maximum value
    cut_lengths = [0] * (n + 1)

  # Base case: a rod of length 0 has a value of 0
    max_value[0] = 0

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            current_value = prices[j - 1] + max_value[i - j]

            if current_value > max_value[i]:
                max_value[i] = current_value
                cut_lengths[i] = j

    cut_list = []
    i = n
    while i > 0:
        cut_list.append(cut_lengths[i])
        i -= cut_lengths[i]

    return cut_list[::-1]

# Example 
n = 8 
prices = [1, 5, 8, 9, 10, 17, 17, 20] 
recommended_cuts = cut_rod(n, prices)
print("Recommended lengths:", recommended_cuts)
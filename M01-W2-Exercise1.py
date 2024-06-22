def max_kernel(num_list, k):
  # Initialize result list
  result = []
  # Check and process the correct input
  if (len(num_list) > k) and (k > 0):
    # index i run from 0 to the length of the list - k
    for i in range(len(num_list) - k + 1):
      result.append(max(num_list[i:i+k]))
    return result
  # If input is not correct -> return warning
  else:
    return print('Error, please input correct List and number k')

# MAIN PROGRAM
if __name__ == "__main__":
    input_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    print(max_kernel(input_list, k))
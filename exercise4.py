def levenshtein_distance(source_string, target_string):
  len_source = len(source_string)
  len_target = len(target_string)

  # Step 1: Initialize the 2D matrix cover all dimension of 2 string
  matrix = [[0 for _ in range(len_target + 1)] for _ in range(len_source + 1)]

  # Step 2: Initialize the first row and first column of the matrix
  for i in range(len_source + 1):
    matrix[i][0] = i
  for j in range(len_target + 1):
    matrix[0][j] = j

  # Step 3: Fill the value
  # Loop: Fill the row (source):
  for i in range(1, len_source + 1):
    # Loop: Fill the column (target):
    for j in range(1, len_target + 1):
      # Check character from source and target matching -> calculate Cost
      if source_string[i-1] == target_string[j-1]:
        cost = 0
      else:
        cost = 1
      # Add the Minimum value to the matrix
      matrix[i][j] = min(matrix[i-1][j] + 1,
                         matrix[i][j-1] + 1,
                         matrix[i-1][j-1] + cost)
  # Use for Debug <=======
  for i in range(len_source+1):
    print(matrix[i])

  return matrix[len_source][len_target]

# MAIN PROGRAM
if __name__ == "__main__":
    s1 = "kitten"
    s2 = "sitting"
    distance = levenshtein_distance(s1, s2)
    print(f"Levenshtein distance '{s1}' and '{s2}' is {distance}")

    # assert levenshtein_distance ("hi", "hello") == 4.0
    # print ( levenshtein_distance ("hola", "hello") )
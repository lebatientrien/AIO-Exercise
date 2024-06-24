def character_count(word):
  # Initialize a dictionary to store the character counts
  character_statistic = {}
  # Iterate each character in the word
  for char in word:
    # Check if the character is in the dictionary
    if char in character_statistic:
      character_statistic[char] += 1
    # If the character is not in the dictionary, add it with a count of 1
    else:
      character_statistic[char] = 1
  return character_statistic

# MAIN PROGRAM
if __name__ == "__main__":
    assert character_count ("Baby") == {'B': 1 , 'a': 1 , 'b': 1 , 'y': 1}
    print ( character_count ('smiles') )
'!gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko'
file_path = '/content/P1_data.txt'

def word_count(file_path):
  # Initialize an empty dictionary to store the counts
  counter = {}
  # Open and read the file
  with open(file_path, 'r') as file:
    # Read the content of the file
    content = file.read()
    # Split the text into list of words
    list_words = content.split()
    # Iterate over each character in the list of words
    for word in list_words:
      # Convert word into lowercase
      word = word.lower()
      # Check if the word is in the dictionary
      if word in counter:
        counter[word] += 1
      else:
        counter[word] = 1
  return counter

# MAIN PROGRAM
if __name__ == "__main__":
    print(word_count(file_path))

    file_path = '/content/P1_data.txt'
    result = word_count( file_path )
    assert result ['who'] == 3
    print ( result ['man'])
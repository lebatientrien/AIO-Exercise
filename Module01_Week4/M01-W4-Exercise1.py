import streamlit as st


def levenshtein_distance(token1, token2):
    dist = [[0] * (len(token2) + 1) for _ in range(len(token1) + 1)]
    for i in range(len(token1) + 1):
        dist[i][0] = i
    for i in range(len(token2) + 1):
        dist[0][i] = i

    for i in range(1, len(token1) + 1):
        for j in range(1, len(token2) + 1):
            if (token1[i - 1] == token2[j - 1]):
                dist[i][j] = dist[i - 1][j - 1]
            else:
                dist[i][j] = min([dist[i][j - 1], dist[i - 1]
                                 [j], dist[i - 1][j - 1]]) + 1

    return dist[len(token1)][len(token2)]


def load_vocab(file_path):
    with open(file_path, 'r') as f:
        data = f.readlines()
    vocab = sorted(set(line.strip().lower() for line in data))
    return vocab


def main():
    vocabs = load_vocab_file(file_path='Module1/Week4-Streamlit/vocab.txt')
    # print(vocabs)
    st.title('Word Correction using Levenshtein Distance')
    word = st.text_input('Word:')

    if st.button('Compute'):
        leven_dist = dict()

        for vocab in vocabs:
            leven_dist[vocab] = levenshtein_distance(word, vocab)

        sorted_dists = dict(
            sorted(leven_dist.items(), key=lambda item: item[1]))
        correct_word = list(sorted_dists.keys())[0]
        st.write('Correct Word: ', correct_word)
        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)
        col2.write('Distances')
        col2.write(sorted_dists)


if __name__ == "__main__":
    main()

import numpy as np

# Function calculateing the length of a vector


def compute_length_vector(vector):
    return np.sqrt(np.sum(vector*vector))

# Function compute dot product of the vectors


def compute_dot_vector(vector1, vector2):
    return np.sum(vector1 * vector2)

# Function multiplying a matrix by a vector


def compute_multi_vector(matrix_a, vector):
    return np.dot(matrix_a, vector)

# Function multiplying matrix by a matrix


def compute_multi_matrix(matrix_a, matrix_b):
    product = np.multiply(matrix_a, matrix_b)
    return product


if __name__ == "__main__":

    # assuming a vector define below:
    vector1 = np.array([1, 2, 3])
    vector2 = np.array([3, 4, 2])
    matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix2 = np.array([[1, 1, 1], [2, 3, 4], [6, 7, 8]])
    a_matrix = np.array([[-2, 6], [8, -4]])

    print("Tinh vector length: ", compute_length_vector(
        np.array([-2, 4, 9, 21])))
    print("Dot Product: ", compute_dot_vector(
        np.array([0, 1, -1, 2]), np.array([2, 5, 1, 0])))
    print("Multiplying vector by matrix: ",
          compute_multi_vector(vector1, matrix1))
    print("Multiplying matrix by matrix: \n",
          compute_multi_matrix(matrix1, matrix2))

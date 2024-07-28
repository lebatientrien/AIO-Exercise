# ########################
# Create data
# ########################
import numpy as np

# Input training Data


def create_train_data():
    data = [
        ['Sunny', 'Hot', 'High', 'Weak', 'no'],
        ['Sunny', 'Hot', 'High', 'Strong', 'no'],
        ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
        ['Rain', 'Mild', 'High', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
        ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
        ['Overcast', 'Mild', 'High', 'Weak', 'no'],
        ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Mild', 'Normal', 'Weak', 'yes']]
    return np.array(data)


train_data = create_train_data()
print(train_data)

# Function compute prior probability


def compute_prior_probability(train_data):
    # Extract the target column (last column)
    target_column = train_data[:, -1]
    # Find unique classes and their counts
    unique_classes, counts = np.unique(target_column, return_counts=True)
    # Compute prior probabilities
    prior_probability = counts / len(target_column)
    # return dict(zip(unique_classes, prior_probability))
    return prior_probability


print(compute_prior_probability(train_data))
prior_probablity = compute_prior_probability(train_data)
print("P(play tennis = No)", prior_probablity[0])
print("P(play tennis = Yes)", prior_probablity[1])

# Hoàn thiện function compute_conditional_probability để tính likelihood (The probability
# of "A" being True. Given "B" True, P(A|B)) như bên dưới:


def compute_conditional_probability(train_data):
    y_unique = ['no', 'yes']
    conditional_probability = []
    list_x_name = []

    for i in range(0, train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)
        x_conditional_probability = {}

        for x_val in x_unique:
            x_conditional_probability[x_val] = {}
            for y_val in y_unique:
                count_y = np.sum(train_data[:, -1] == y_val)
                count_x_and_y = np.sum(
                    (train_data[:, i] == x_val) & (train_data[:, -1] == y_val))
                x_conditional_probability[x_val][y_val] = count_x_and_y / \
                    count_y if count_y > 0 else 0

        conditional_probability.append(x_conditional_probability)

    return conditional_probability, list_x_name


train_data = create_train_data()
conditional_probability, list_x_name = compute_conditional_probability(
    train_data)
print("Conditional Probability:\n", conditional_probability)
print("List of Unique Feature Values:\n", list_x_name)

# This function is used to return the index of the feature name


def get_index_from_value(feature_name, list_features):
    return np.where(list_features == feature_name)[0][0]

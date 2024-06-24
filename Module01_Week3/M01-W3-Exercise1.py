import torch
import torch.nn as nn

# Build class Softmax and inherit from nn.Module


class Softmax(nn.Module):
    def __init__(self):
        # Inherit the Init from parent class nn.Module
        super().__init__()

    def forward(self, data):
        exponental_data = torch.exp(data)
        # Calculate the sum of each element
        # keepdim=True for keep the direction
        return exponental_data/torch.sum(exponental_data, dim=0, keepdim=True)


class SoftmaxStable(nn.Module):
    def __init__(self):
        # Inherit the Init from parent class nn.Module
        super().__init__()

    def forward(self, data):
        c = torch.max(data)
        exponental_data = torch.exp(data - c)
        return exponental_data/torch.sum(exponental_data, dim=0, keepdim=True)


# MAIN PROGRAM
if __name__ == '__main__':
    data = torch.Tensor([1, 2, 3])

    softmax = Softmax()
    output1 = softmax(data)
    print(output1)

    softmax_stable = SoftmaxStable()
    output2 = softmax_stable(data)
    print(output2)

import torch

# This script checks if MPS (Metal Performance Shaders) is available for PyTorch.
# If it is, it sets the device to 'mps', otherwise it defaults to 'cpu'.
dev = torch.device('cpu')
if torch.backends.mps.is_available():
    print("mps")
    dev = torch.device('mps')
print(dev)
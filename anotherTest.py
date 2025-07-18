import torch
dev= torch.device('cpu')
if torch.backends.mps.is_available():
    print("mps")
    dev=torch.device('mps')
print(dev)
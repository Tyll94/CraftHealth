import torch

# Check if CUDA is available
print("CUDA available: ", torch.cuda.is_available())

# If CUDA is available, perform a simple tensor operation on the GPU
if torch.cuda.is_available():
    x = torch.rand(5, 5).cuda()
    print(x)
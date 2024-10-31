import torch
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Select device for PyTorch")
    parser.add_argument('--cuda', action='store_true', help='Use CUDA if available')
    args = parser.parse_args()

    # Select device
    device = torch.device("cuda:0" if args.cuda and torch.cuda.is_available() else "cpu")
    
    # Print the selected device
    print('Using device:', device, file=sys.stderr)

if __name__ == "__main__":
    main()

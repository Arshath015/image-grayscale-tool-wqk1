import sys
from PIL import Image

def to_grayscale(input_path, output_path):
    img = Image.open(input_path).convert('L')
    img.save(output_path)
    print(f"Saved grayscale image to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py input.jpg output.jpg")
        sys.exit(1)
    to_grayscale(sys.argv[1], sys.argv[2])

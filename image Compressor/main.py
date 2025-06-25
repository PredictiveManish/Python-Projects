import os
import sys
from PIL import Image

def compressMe(file, verbose=False):
    filepath = os.path.join(os.getcwd(), file)

    picture = Image.open(filepath)

    if picture.mode != "RGB":
        picture = picture.convert("RGB")

    compressed_filename = "Compressed_" + file
    picture.save(compressed_filename,
                 "JPEG",
                 optimize=True,
                 quality=10)

    if verbose:
        print(f"{file} compressed --> {compressed_filename}")

    return os.path.getsize(compressed_filename)  


def main():
    verbose = False
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "-v":
            verbose = True

    
    target_kb = float(input("Enter target total size of compressed folder (in KB): "))
    target_bytes = target_kb * 1024

    cwd = os.getcwd()
    formats = ('.jpg', '.jpeg', '.png')
    total_size = 0  

    for file in os.listdir(cwd):
        if os.path.splitext(file)[1].lower() in formats:
            print(f'Compressing {file}...')

            compressed_size = compressMe(file, verbose)
            total_size += compressed_size

            print(f"Total compressed size so far: {round(total_size / 1024, 2)} KB")

            if total_size >= target_bytes:
                print("\nTarget folder size reached.")
                break

    print("\nDone compressing!")

if __name__ == "__main__":
    main()

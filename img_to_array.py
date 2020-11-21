import os
from PIL import Image

f = "batman.png"


def main():
    img = Image.open(os.path.join("images", f))  # Open the file
    # Converts image to greyscale (not binary)
    # The algorythm used with mode "1" (binary) doesn't work well in this instance
    img = img.convert("L")
    px = img.load()  # Put the pixels in an array
    print(img.format, img.size, img.mode)

    print("batman = [", flush=False)
    for y in range(img.size[1]):  # for each lines of pixels
        print("[", end="", flush=False)
        for x in range(img.size[0]):  # for each pixels from that line
            if px[x, y] == 0:
                # end="" means to not print a new line
                print(0, end="", flush=False)
            else:
                # flush=false means to not write to the screen yet
                print(1, end="", flush=False)
            if x < img.size[0] - 1:
                # Do not add a comma at the end if it's the last item
                print(",", end="", flush=False)
        print("]", end="", flush=False)
        if y < img.size[1] - 1:
            # Do not add a comma at the end if it's the last item
            print(",", end="", flush=False)
        print()  # Prints a new line
    print("]")


if __name__ == "__main__":
    main()

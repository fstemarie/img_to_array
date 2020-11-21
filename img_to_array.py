import os
from PIL import Image

inverse = True
f = "ww.png"

def main():
    img = Image.open(os.path.join("images", f))  # Open the file
    px = img.load()  # Put the pixels in an array

    t = "# {}\n{} = [\n".format(img.size, f[0: -4])
    for y in range(img.size[1]):  # for each lines of pixels
        t += "["
        for x in range(img.size[0]):  # for each pixels from that line
            if px[x, y] == 0:
                # end="" means to not print a new line
                t += "1" if inverse else "0"
            else:
                # flush=false means to not write to the screen yet
                t += "0" if inverse else "1"
            # Do not add a comma at the end if it's the last item
            t += "," if x < img.size[0] - 1 else ""
        t += "]"
        if y < img.size[1] - 1:
            # Do not add a comma at the end if it's the last item
            t += ","
        t += "\n" # Add a new line
    t += "]\n"

    out = open(os.path.join("output", f[0: -4] + ("_inverse" if inverse else "") + ".py"), "w")
    out.write(t)
    out.close()
    t = t.replace(",", "").replace("[", "").replace("]", "")
    print(t)


if __name__ == "__main__":
    main()

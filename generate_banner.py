from PIL import Image, ImageDraw

# Settings — matches design.png style
block  = 36    # size of each pixel block
gap    = 5     # transparent gap between blocks
cell   = block + gap
color  = (232, 123, 76)    # warm orange (matches design.png)
outline = (80, 40, 20)     # dark brown inner outline
pad    = 50    # outer padding

font = {
    "T": ["11111","00100","00100","00100","00100","00100","00100"],
    "U": ["10001","10001","10001","10001","10001","10001","11111"],
    "R": ["11110","10001","10001","11110","10100","10010","10001"],
    "Z": ["11111","00001","00010","00100","01000","10000","11111"],
    "A": ["01110","10001","10001","11111","10001","10001","10001"],
    " ": ["00000"]*7,
    "B": ["11110","10001","10001","11110","10001","10001","11110"],
    "S": ["01111","10000","10000","01110","00001","00001","11110"],
    "K": ["10001","10010","10100","11000","10100","10010","10001"],
}

line1 = "TURZA"
line2 = "BASAK"

cols = max(len(line1), len(line2))
rows = 7

img_w = pad * 2 + cols * 5 * cell + (cols - 1) * cell
img_h = pad * 2 + rows * cell * 2 + cell * 2

# RGBA — transparent background works on any GitHub theme
img  = Image.new("RGBA", (img_w, img_h), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

def draw_block(x0, y0):
    """Matches design.png: solid fill + two concentric dark outlines inside."""
    b = block
    # Solid orange fill
    draw.rectangle([x0, y0, x0+b-1, y0+b-1], fill=color)
    # First inner outline (inset 3px)
    draw.rectangle([x0+3, y0+3, x0+b-4, y0+b-4], outline=outline, width=1)
    # Second inner outline (inset 6px)
    draw.rectangle([x0+6, y0+6, x0+b-7, y0+b-7], outline=outline, width=1)

def draw_word(word, row_y):
    total_w = len(word) * 5 * cell + (len(word) - 1) * cell
    x_start = (img_w - total_w) // 2
    x_offset = x_start
    for char in word:
        pattern = font[char]
        for r, row in enumerate(pattern):
            for c, val in enumerate(row):
                if val == "1":
                    draw_block(x_offset + c * cell, row_y + r * cell)
        x_offset += 5 * cell + cell

draw_word(line1, pad)
draw_word(line2, pad + rows * cell + cell * 2)

img.save("banner.png")
print(f"Saved banner.png  ({img_w}x{img_h})")

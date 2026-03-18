from PIL import Image, ImageDraw

# Settings
block  = 22   # size of each pixel block
gap    = 4    # dark gap between blocks
cell   = block + gap
color  = (250, 105, 105)   # #FA6969
dark   = (22,  27,  34)    # #161b22  (inner groove)
bg     = (13,  17,  23)    # #0d1117  (background)
pad    = 40   # outer padding

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

cols  = max(len(line1), len(line2))
rows  = 7   # font height in pixels

img_w = pad * 2 + cols * 5 * cell + (cols - 1) * cell
img_h = pad * 2 + rows * cell * 2 + cell * 2   # 2 rows + row gap

img  = Image.new("RGB", (img_w, img_h), bg)
draw = ImageDraw.Draw(img)

def draw_block(x0, y0):
    """Draw one pixel block: outer coral → dark groove → inner coral."""
    # Outer fill
    draw.rectangle([x0, y0, x0 + block, y0 + block], fill=color)
    # Dark inner ring (inset 2px)
    draw.rectangle([x0 + 2, y0 + 2, x0 + block - 2, y0 + block - 2], fill=dark)
    # Inner coral fill (inset 4px)
    draw.rectangle([x0 + 4, y0 + 4, x0 + block - 4, y0 + block - 4], fill=color)

def draw_word(word, row_y):
    total_w = len(word) * 5 * cell + (len(word) - 1) * cell
    x_start = (img_w - total_w) // 2
    x_offset = x_start
    for char in word:
        pattern = font[char]
        for r, row in enumerate(pattern):
            for c, val in enumerate(row):
                if val == "1":
                    bx = x_offset + c * cell
                    by = row_y  + r * cell
                    draw_block(bx, by)
        x_offset += 5 * cell + cell   # letter width + 1-cell gap

draw_word(line1, pad)
draw_word(line2, pad + rows * cell + cell * 2)

img.save("banner.png")
print(f"Saved banner.png  ({img_w}x{img_h})")

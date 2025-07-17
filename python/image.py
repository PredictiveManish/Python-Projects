from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Small logo dimensions
width, height = 250, 100
bg_color = (255, 255, 255)  # white background

# Create image canvas
img = Image.new("RGB", (width, height), color=bg_color)
draw = ImageDraw.Draw(img)

# --- Draw mini waveform ---
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(4 * x) * 10 + height // 2
for i in range(len(x) - 1):
    draw.line([(i + 10, y[i]), (i + 11, y[i + 1])], fill=(33, 150, 243), width=1)

# --- Add compact logo text ---
try:
    font_main = ImageFont.truetype("arial.ttf", 16)
    font_sub = ImageFont.truetype("arial.ttf", 10)
except:
    font_main = ImageFont.load_default()
    font_sub = ImageFont.load_default()

# Centered or slightly shifted
draw.text((130, 30), "NoiseNet", font=font_main, fill=(0, 0, 0))
draw.text((130, 50), "AI for Sound-Aware Cities", font=font_sub, fill=(80, 80, 80))

# Save + preview
img.save("noisenet_small_logo.png")
img.show()

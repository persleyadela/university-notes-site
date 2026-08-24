from PIL import Image
import glob

for f in glob.glob("*.jpg"):
    img = Image.open(f)
    out = f.replace(".jpg", ".webp")
    img.save(out, "WEBP", quality=75)
    print(out)

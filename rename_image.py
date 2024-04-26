from PIL import Image
import os

dir = "tazab_crop"  #data_dir

#change namne of images in the folder
for count, filename in enumerate(os.listdir(dir)):
    file = os.path.join(dir, filename)
    im = Image.open(file)
    im.save(os.path.join(dir, f"image_{count}.jpg"))
    os.remove(file)
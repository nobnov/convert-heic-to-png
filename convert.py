import glob

import pyheif
from PIL import Image
from tqdm import tqdm

ORIG_DIR = "original/"
CONV_DIR = "convert/"


def conv(image_path):
    heif_file = pyheif.read(image_path)
    data = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )

    dir_name = image_path.replace("HEIC", "png").replace(ORIG_DIR, CONV_DIR)
    data.save(dir_name, "PNG")


lst = glob.glob(ORIG_DIR + "*.HEIC")
for i, l in enumerate(tqdm(lst)):
    conv(l)

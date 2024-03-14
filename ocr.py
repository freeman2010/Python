from PIL import Image
import os
import pytesseract
import sys

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def change_file_extension(filename, new_extension):
  file_name, _ = os.path.splitext(filename)
  new_filename = file_name + new_extension
  return new_filename

def process_image_file(filename):
  try:
    img = Image.open(filename)
    ocrText = pytesseract.image_to_string(img, timeout=5)
    txt_filename = change_file_extension(filename, ".txt")

    with open(txt_filename, "w", encoding="utf-8") as f:
        f.write(ocrText)
    print(f"Found {filename} and wrote to {txt_filename}")
  except Exception as err:
    print(f"Processing of {filename} failed due to error: {err}")

def main(argv):
  for filename in os.listdir("."):
    if filename not in ['.', '..']:
      nameParts = filename.split(".")
      if nameParts[-1].lower() in ["gif", "png", "jpg", "jpeg", "tif", "tiff"]:
        process_image_file(filename)

if __name__ == "__main__":
    main(sys.argv[1:])
import pytesseract
import PIL.Image

def read_arabic_text_from_txt_file(file_name):
  text = pytesseract.image_to_string(PIL.Image.open(file_name), lang='ara')
  return text

if __name__ == "__main__":
  text = read_arabic_text_from_txt_file("my_arabic_text.txt")
  print(text)
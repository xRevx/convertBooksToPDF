import os
import pyautogui as py
import time
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

number_of_pages = 134
book_name = "saprutit"
book_path = os.path.join("C:\\books", book_name)

os.makedirs(book_path, exist_ok=True)
time.sleep(5)
s = "aaaaaaaaaaa"


def increment_string(s):
    s_list = list(s)

    # Find the last character and increment it until 'z' is reached
    i = len(s_list) - 1
    while i >= 0 and s_list[i] == 'z':
        s_list[i] = 'a'
        i -= 1

    if i >= 0:
        # Increment the last non-'z' character
        s_list[i] = chr(ord(s_list[i]) + 1)
    else:
        # If all characters were 'z', add 'a' to the beginning
        s_list = ['a'] + s_list

    return ''.join(s_list)


for i in range(number_of_pages):
    s = increment_string(s)
    page = py.screenshot(region=(650,170, 650, 850))
    page_path = os.path.join(book_path, s + ".png")  # Corrected filename
    page.save(page_path)
    py.press("right")
    time.sleep(0.45)

output_pdf = os.path.join(book_path, book_name + ".pdf")  # Specify a valid PDF filename
input_folder = book_path
c = canvas.Canvas(output_pdf, pagesize=letter)

png_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]

for png_file in png_files:
    image_path = os.path.join(input_folder, png_file)
    img = Image.open(image_path)
    width, height = img.size
    c.setPageSize((width, height))
    c.drawImage(image_path, 0, 0, width, height)
    c.showPage()

c.save()


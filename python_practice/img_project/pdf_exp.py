# add image to PDF via PyMuPDF

import fitz

img_file = "sign_img.png"
source_file = "AWScosts.pdf"
new_file = "test.pdf"

img_rect = fitz.Rect(300,350,500,500)

document = fitz.open(source_file)
page = document[0]
page.insert_image(img_rect,filename=img_file)
document.save(new_file)


from wand.image import Image as Img
from PIL import Image
import pytesseract

def crop_image(filename,cropdict):
    img = Image.open(filename)
    dimensions = get_crop_dim()
    crop_img = img.crop((dimensions['x1'],dimensions['y1'], dimensions['x2'], dimensions['y2']))
    crop_img.save(path+cropped_image_name)

def get_crop_dim():
    return {'x1':10, 'y1':10, 'x2':50, 'y2':50}

with Img(filename=path+pdf_name, resolution=300) as img:
    img.compression_quality = 99
    img.save(filename=path+)

path = '/home/tr-dt-102/Desktop/'
pdf_name = 'ROCIA_CV.pdf'
image_name = pdf_name.replace('.pdf','.jpg')
cropped_image_name =image_name.replace('.pdf','.jpg')

text = pytesseract.image_to_string(Image.open('image.jpg'))
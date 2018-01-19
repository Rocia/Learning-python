from wand.image import Image as Img
from PIL import Image
import pytesseract
import PyPDF2, sys

def crop_image(filename,cropdict):
    img = Image.open(filename)
    dimensions = get_crop_dim()
    crop_img = img.crop((dimensions['x1'],dimensions['y1'], dimensions['x2'], dimensions['y2']))
    crop_img.save(path+cropped_image_name)

def get_crop_dim():
    return {'x1':10, 'y1':10, 'x2':50, 'y2':50}

def extract_text(imagename):
    text = pytesseract.image_to_string(Image.open(imagename))
    return text

def get_text(image_name, Pgno):
    for i in range(0,Pgno):
        if i > 0:
            current_img_name =  image_name+i
        else:
            current_img_name = image_name
        extract_text(current_img_name)
            

def pdf_to_jpg(path, pdf_name,image_name):
    try:
        noPages = get_num_of_pages(path+pdf_name)
        with Img(filename=path+pdf_name, resolution=300) as img:
            img.compression_quality = 99
            img.save(filename=path+image_name)
        return noPages
    except:
        sys.exit("Failure in processing your file")

def get_num_of_pages(pdf):
    pdfFileObj = open(pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    return pdfReader.numPages

path = '/home/tr-dt-102/Desktop/'
pdf_name = 'ROCIA_CV.pdf'
image_name = pdf_name.replace('.pdf','.jpg')
cropped_image_name =image_name.replace('.pdf','.jpg')

if __name__ == "__main__":
    pdf_to_jpg(path, pdf_name,image_name)
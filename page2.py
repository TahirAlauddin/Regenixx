from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import ELEVENSEVENTEEN
from io import BytesIO
from constants import *
from textwrap import wrap
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import reportlab
import sys
import os
from decimal import Decimal

# Register fonts
fonts_directory = 'fonts'
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    fonts_directory = os.path.join(sys._MEIPASS, 'fonts')
reportlab.rl_config.TTFSearchPath.append(fonts_directory)
pdfmetrics.registerFont(TTFont('Montserrat-Black', r'Montserrat-Black.ttf'))
pdfmetrics.registerFont(TTFont('Montserrat-Regular', r'Montserrat-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Montserrat-Bold', r'Montserrat-Bold.ttf'))


def writeServicesPlan1(canvas: Canvas, services: list, discount: int):
    prices = [Decimal(service[1]) * int(service[2]) for service in services]
    canvas.setFillColor(HexColor(PLAN1_COLOR))
    y = SERVICE1_Y

    for service in services:
        if str(service[2]).isdigit() and int(service[2]) > 1:
            service_title = f'{service[0]} ({service[2]}x)'
            service_price = int(service[1]) * int(service[2])
        else:
            service_title = f'{service[0]}'
            service_price = service[1]
        canvas.setFont("Montserrat-Regular", 10)
        canvas.drawRightString(270, y,  f'${service_price}')  
        canvas.setFont("Montserrat-Bold", 9)

        service_text = wrap(service_title, width=30, break_long_words=True)
        for service_line in service_text:
            canvas.drawString(PLAN1_SERVICES_X, y, service_line)
            y -= 10

        y -= MARGIN_BETWEEN_SERVICES

    # Discount Price
    subtotal_price = sum(prices)
    discount_price = (sum(prices) * discount) / 100
    # String Formats
    subtotal_price_string = '{:.2f}'.format(subtotal_price)
    total_price_string = '{:.2f}'.format(subtotal_price-discount_price)
    discounted_price_string = '{:.2f}'.format(discount_price)

    canvas.setFont("Montserrat-Black", 11)
    canvas.drawString(PLAN1_SUBTOTAL_PRICE_X, SUBTOTAL_PRICE_Y, f'${subtotal_price_string}') 
    canvas.drawString(PLAN1_DISCOUNT_PRICE_X, DISCOUNT_PRICE_Y, f'{discount}% OFF (${discounted_price_string})') 
        
    # Change Color for Total Price
    canvas.setFillColor(HexColor(PLAN1_TOTAL_PRICE_COLOR))
    # Total Price
    canvas.drawString(PLAN1_TOTAL_PRICE_X, TOTAL_PRICE_Y, f'${total_price_string}') 


def writeServicesPlan2(canvas: Canvas, services: list, discount: int):
    prices = [Decimal(service[1]) * int(service[2]) for service in services]
    canvas.setFillColor(HexColor(PLAN2_COLOR))
    y = SERVICE1_Y

    for service in services:
        if str(service[2]).isdigit() and int(service[2]) > 1:
            service_title = f'{service[0]} ({service[2]}x)'
            service_price = int(service[1]) * int(service[2])
        else:
            service_title = f'{service[0]}'
            service_price = service[1]
        canvas.setFont("Montserrat-Regular", 10)
        canvas.drawRightString(510, y,  f'${service_price}') 
        canvas.setFont("Montserrat-Bold", 9)

        service_text = wrap(service_title, width=30, break_long_words=True)
        for service_line in service_text:
            canvas.drawString(PLAN2_SERVICES_X, y, service_line)
            y -= 10

        canvas.setFont("Montserrat-Regular", 10)
        y -= MARGIN_BETWEEN_SERVICES

    # Discount Price
    subtotal_price = sum(prices)
    discount_price = (sum(prices) * discount) / 100

    # String Formats
    subtotal_price_string = '{:.2f}'.format(subtotal_price)
    total_price_string = '{:.2f}'.format(subtotal_price-discount_price)
    discounted_price_string = '{:.2f}'.format(discount_price)

    canvas.setFont("Montserrat-Black", 11)
    canvas.drawString(PLAN2_SUBTOTAL_PRICE_X, SUBTOTAL_PRICE_Y, f'${subtotal_price_string}') 
    canvas.drawString(PLAN2_DISCOUNT_PRICE_X, DISCOUNT_PRICE_Y, f'{discount}% OFF (${discounted_price_string})') 

    # Change Color for Total Price
    canvas.setFillColor(HexColor(PLAN2_TOTAL_PRICE_COLOR))
    # Total Price
    canvas.drawString(PLAN2_TOTAL_PRICE_X, TOTAL_PRICE_Y, f'${total_price_string}') 
        

def writeServicesPlan3(canvas: Canvas, services: list, discount: int):
    prices = [Decimal(service[1]) * int(service[2]) for service in services]
    canvas.setFillColor(HexColor(PLAN3_COLOR))
    y = SERVICE1_Y

    for service in services:
        if str(service[2]).isdigit() and int(service[2]) > 1:
            service_title = f'{service[0]} ({service[2]}x)'
            service_price = int(service[1]) * int(service[2])
        else:
            service_title = f'{service[0]}'
            service_price = service[1]

        canvas.setFont("Montserrat-Regular", 10)
        canvas.drawRightString(745, y,  f'${service_price}') 
        canvas.setFont("Montserrat-Bold", 9)

        service_text = wrap(service_title, width=30, break_long_words=True)
        for service_line in service_text:
            canvas.drawString(PLAN3_SERVICES_X, y, service_line)
            y -= 10

        canvas.setFont("Montserrat-Regular", 10)
        y -= MARGIN_BETWEEN_SERVICES


    # Discount Price
    subtotal_price = sum(prices)
    discount_price = (sum(prices) * discount) / 100
    # String Formats
    subtotal_price_string = '{:.2f}'.format(subtotal_price)
    total_price_string = '{:.2f}'.format(subtotal_price-discount_price)
    discounted_price_string = '{:.2f}'.format(discount_price)

    canvas.setFont("Montserrat-Black", 11)
    canvas.drawString(PLAN3_SUBTOTAL_PRICE_X, SUBTOTAL_PRICE_Y, f'${subtotal_price_string}') 
    canvas.drawString(PLAN3_DISCOUNT_PRICE_X, DISCOUNT_PRICE_Y, f'{discount}% OFF (${discounted_price_string})') 

    # Change Color for Total Price    
    canvas.setFillColor(HexColor(PLAN3_TOTAL_PRICE_COLOR))
    # Total Price
    canvas.drawString(PLAN3_TOTAL_PRICE_X, TOTAL_PRICE_Y,  f'${total_price_string}') 
        

# Draw an image on the canvas
def draw_image_plan1(canvas: Canvas, image):
    canvas.drawImage(image, IMAGE_MARGIN_LEFT, IMAGE_MARGIN_BOTTOM,
                            IMAGE_WIDTH, IMAGE_HEIGHT, mask='auto')

def draw_image_plan2(canvas: Canvas, image):
    canvas.drawImage(image,
                                (IMAGE_MARGIN_LEFT*2) + IMAGE_WIDTH + 3,   # x
                                IMAGE_MARGIN_BOTTOM,                       # y
                                IMAGE_WIDTH,                               # width
                                IMAGE_HEIGHT, mask='auto')                 # height

def draw_image_plan3(canvas: Canvas, image):
    canvas.drawImage(image, (IMAGE_MARGIN_LEFT*3) + (IMAGE_WIDTH*2) + 6, 
                                IMAGE_MARGIN_BOTTOM, IMAGE_WIDTH,
                                IMAGE_HEIGHT, mask='auto')

def writePage2(canvas: Canvas, image_plan1, image_plan2, image_plan3,
               services_plan1, services_plan2, services_plan3,
               discount_plan1, discount_plan2, discount_plan3):
    # Create a new PDF file with a single page
    draw_image_plan1(canvas, image_plan1)
    draw_image_plan2(canvas, image_plan2)
    draw_image_plan3(canvas, image_plan3)

    writeServicesPlan1(canvas, services_plan1, discount_plan1)
    writeServicesPlan2(canvas, services_plan2, discount_plan2)
    writeServicesPlan3(canvas, services_plan3, discount_plan3)

def main():
    image_plan1 = 'pdf-images/image1.png'
    image_plan2 = 'pdf-images/image2.png'
    image_plan3 = 'pdf-images/image3.png'

    template_pdf_path='PDFs/Patient Program PDF Template.pdf'
    output_pdf_path = f'PDFs/page2.pdf'
    
    packet = BytesIO()
    canvas = Canvas(packet, pagesize=ELEVENSEVENTEEN)
    services_plan2 = services_plan3 = services_plan1 = [
        ['Service 1 Long Text whichtakes takessignificantly more space than other', '63'],
        ['Service 2 Long Text whichtakes takessignificantly more', '143'],
        ['Service 3 Long ', '742'],
        ['Service 4 Long takessignificantly more', '1233'],
        ['Service 5 Long', '200'],
        ['Service 5 Long, This is also a long text which takes more space', '7687'],
    ]
    writePage2(canvas, image_plan1, image_plan2, image_plan3, 
               services_plan1, services_plan2, services_plan3, 
               discount_plan1=15, discount_plan2=10, discount_plan3=5)

    canvas.save()

    output_pdf = PdfFileWriter()
    template_pdf = PdfFileReader(open(template_pdf_path, "rb"))
    canvas_pdf = PdfFileReader(packet)

    templatePage2 = template_pdf.pages[1]
    templatePage2.mergePage(canvas_pdf.pages[0])
    output_pdf.addPage(templatePage2)
            
    #move to the beginning of the StringIO buffer
    packet.seek(0)
    
    # finally, write "output" to a real file
    output_stream = open(output_pdf_path, "wb")

    output_pdf.write(output_stream)
    output_stream.close()


if __name__ == '__main__':
    main()

from page1 import *
from page2 import *
import os
import time


def get_available_filename(filename):
    """
    Check if the given filename exists in the current directory.
    If it exists, append a number to the filename until an available filename is found.
    """
    # Check if the original filename exists
    if not os.path.exists(filename):
        return filename

    # If the original filename exists, find an available filename
    base, ext = os.path.splitext(filename)
    i = 1
    while True:
        new_filename = f"{base} ({i}){ext}"
        if not os.path.exists(new_filename):
            return new_filename
        i += 1


def generatePDF(patients_name: str, patients_date_of_birth: str, diagnosis: str,
                image_plan1: str, image_plan2: str, image_plan3: str,
                services_plan1, services_plan2, services_plan3, discount_plan1,
                discount_plan2, discount_plan3,
                template_pdf_path=None, output_pdf_path=None,
                signal=None):
    
    if not output_pdf_path:
        output_pdf_path = f'PDFs/{patients_name} {patients_date_of_birth}.pdf'
    if not template_pdf_path:
        template_pdf_path='PDFs/Patient Program PDF Template.pdf'

    packet1 = BytesIO()
    packet2 = BytesIO()
    canvas1 = Canvas(packet1, pagesize=ELEVENSEVENTEEN)
    canvas2 = Canvas(packet2, pagesize=ELEVENSEVENTEEN)
    writePage1(canvas1, patients_name, patients_date_of_birth, diagnosis)

    if signal:
        signal.emit('DRAWING IMAGES')
    
    writePage2(canvas2, image_plan1, image_plan2, image_plan3, 
               services_plan1, services_plan2, services_plan3, 
               discount_plan1, discount_plan2, discount_plan3)

    canvas1.save()
    canvas2.save()

    if signal:
        signal.emit('WRITING PAGES')

    output_pdf = PdfFileWriter()
    template_pdf = PdfFileReader(open(template_pdf_path, "rb"))
    canvas_pdf1 = PdfFileReader(packet1)
    canvas_pdf2 = PdfFileReader(packet2)

    templatePage1 = template_pdf.pages[0]
    templatePage2 = template_pdf.pages[1]
    templatePage1.mergePage(canvas_pdf1.pages[0])
    templatePage2.mergePage(canvas_pdf2.pages[0])

    if signal:
        signal.emit('MERGING PAGES')

    output_pdf.addPage(templatePage1)
    output_pdf.addPage(templatePage2)

    if signal:
        signal.emit('SAVING FILE')
            
    #move to the beginning of the StringIO buffer
    packet1.seek(0)
    packet2.seek(0)

    output_pdf_path = get_available_filename(output_pdf_path)
    
    # finally, write "output" to a real file
    output_stream = open(output_pdf_path, "wb")

    output_pdf.write(output_stream)
    output_stream.close()

    if signal:
        signal.emit('DONE! THANKS FOR WAITING 😀')
        time.sleep(1)
        signal.emit('')


if __name__ == '__main__':
    generatePDF('Tahir', 'March 29, 2023', 'Severly ill', 'pdf-images/image1.png',
                'pdf-images/image2.png', 'pdf-images/image3.png', None, None, None, 5)
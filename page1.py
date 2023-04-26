from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import ELEVENSEVENTEEN
from textwrap import wrap
from io import BytesIO
from datetime import datetime

TEXT_LEFT_MARGIN = 180
format_string = "%B %d, %Y"


def writeTodayDate(canvas: Canvas):
    canvas.drawString(TEXT_LEFT_MARGIN, 160-2, datetime.now().strftime(format_string)) # DATE

def writePatientsName(canvas: Canvas, patients_name: str):
    canvas.drawString(TEXT_LEFT_MARGIN, 135-2, patients_name) # NAME

def writePatientsDateOfBirth(canvas: Canvas, date_of_birth: str):
    canvas.drawString(TEXT_LEFT_MARGIN, 110-2, date_of_birth) # DATE OF BIRTH

def writeDiagnosis(canvas: Canvas, diagnosis: str):
    diagnosis_list = wrap(diagnosis, width=50)
    for idx, diagnosis in enumerate(diagnosis_list):
        canvas.drawString(TEXT_LEFT_MARGIN, (85)-(idx *15) - 2, diagnosis, wordSpace=1) # DIAGNOSIS

def writePage1(canvas: Canvas, patients_name: str, patients_date_of_birth: str,
               diagnosis: str):

    # Write Text to IO
    writeTodayDate(canvas)
    writePatientsName(canvas, patients_name)
    writePatientsDateOfBirth(canvas, patients_date_of_birth)
    writeDiagnosis(canvas, diagnosis)



def main():
    diagnosis = "This line is taking significantly more space than the space. The PDF can't show all this text. More or less, it could fill in an entire paragraph without issue."
    patients_name = "John Doe"
    patients_date_of_birth = datetime(1999, 12, 12).strftime(format_string)
    
    template_pdf_path='PDFs/Patient Program PDF Template.pdf'
    output_pdf_path = f'PDFs/{patients_name}-{patients_date_of_birth}.pdf'
    
    packet = BytesIO()
    canvas = Canvas(packet, pagesize=ELEVENSEVENTEEN)
    
    writePage1(canvas, patients_name, patients_date_of_birth, diagnosis)
    canvas.save()

    output_pdf = PdfFileWriter()
    template_pdf = PdfFileReader(open(template_pdf_path, "rb"))
    canvas_pdf = PdfFileReader(packet)

    templatePage1 = template_pdf.pages[0]
    templatePage1.mergePage(canvas_pdf.pages[0])
    output_pdf.addPage(templatePage1)
            
    #move to the beginning of the StringIO buffer
    packet.seek(0)
    
    # finally, write "output" to a real file
    output_stream = open(output_pdf_path, "wb")

    output_pdf.write(output_stream)
    output_stream.close()


if __name__ == '__main__':
    main()

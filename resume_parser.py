from PyPDF2 import PdfReader

def extract_text_from_pdf(file):

    pdf = PdfReader(file)

    text = ""

    for page in pdf.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text
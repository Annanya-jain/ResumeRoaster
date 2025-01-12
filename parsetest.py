'''
from pypdf import PdfReader

reader = PdfReader("Resume-Annanya.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"
print(text)

'''
import PyPDF2

def function1(file_obj):
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file_obj)
    
    # Initialize a variable to store the extracted text
    text_content = ''
    
    # Iterate through all pages and extract text
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text_content += page.extract_text()  # Extract text from the page
    
    return text_content

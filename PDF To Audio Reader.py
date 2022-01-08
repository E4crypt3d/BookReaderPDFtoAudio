import PyPDF2
import pyttsx3

# By E4crypt3d
pdffile = open(input('Enter the book name: ')+'.pdf', 'rb')
page_no = int(input("Enter the page number from which you want the system to start reading text: "))

pdf_Reader = PyPDF2.PdfFileReader(pdffile)
pages = pdf_Reader.numPages

speaker = pyttsx3.init()
for num in range((page_no-1), pages):
    page = pdf_Reader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
from PyPDF2 import PdfWriter, PdfReader

def pdf_protect(filename, pwd):

    out = PdfWriter()

    file = PdfReader(filename)

    num = len(file.pages)

    for idx in range(num):
        
        page = file.pages[idx]
        out.add_page(page)

    password = pwd

    out.encrypt(password)

    with open("myfile_encrypted.pdf", "wb") as f:
        out.write(f)

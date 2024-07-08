""" I've got some password-protected PDFs, and it annoyed me not to be able to copy-and-paste from them. So, I had to remove the password-protection """ 


import PyPDF2

def remove_passwd(pdfname, outname_name, passwd):
    pdf_reader = PyPDF2.PdfReader(pdfname)
    if pdf_reader.is_encrypted:
        pdf_reader.decrypt(passwd)
    
    pdf_writer = PyPDF2.PdfWriter()
    
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])
    
    with open(outname_name, 'wb') as f:
        pdf_writer.write(f)

pdfname = '/home/kali/ibra/testing/mypdf.pdf'
outname_name = '/home/kali/ibra/testing/out/out.pdf'
passwd = '2C|uXz.PEn~mxLN2,J~SI1:rH#y?t5'

remove_passwd(pdfname, outname_name, passwd)

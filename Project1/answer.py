import PyPDF2, os
from PyPDF2 import PdfFileReader

if os.path.isdir("./content"):
    if os.path.isfile('./content/testfile.pdf'):
        if os.path.isfile('./content/output.txt'):
            f = open('./content/testfile.pdf','rb')
            file1=open('./content/output.txt','w+')
            pdf_reader = PyPDF2.PdfReader(f)
            print('Number of pages ' + str(len(pdf_reader.pages)))
            for page in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page]
                page_text = page.extract_text()
                file1.writelines(page_text)
            f.close()
            file1.close()
            print('SUCCESSFUL! contents read from testfile.pdf and stored in output.txt')
        else:
            print('OUTPUT File doesnt exist')
    else:
        print('TEST File doesnt exist')
else:
    print('CONTENT Folder doesnt exist')
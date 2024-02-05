import PyPDF2, os
from PyPDF2 import PdfFileReader

def project2():
    response = ''
    root = "./content"
    if os.path.isdir(root):
        print(os.listdir(root))
        for dir, subdirs, files in os.walk(root, topdown=True):
            print('Found directory: %s' % dir)
            if(os.path.exists(os.path.join(dir, 'output.txt'))):
                for file in files:
                    print(os.path.join(dir, file))
                    if(file).endswith('.pdf'):
                        pdf_file = open(os.path.join(dir, file),'rb')
                        output_file=open(os.path.join(dir, 'output.txt'),'w+')
                        pdf_reader = PyPDF2.PdfReader(pdf_file)
                        print('Number of pages ' + str(len(pdf_reader.pages)))
                        print('Enter a page number :')
                        page_num = int(input())
                        page = pdf_reader.pages[page_num-1]
                        page_text = page.extract_text()
                        output_file.writelines(page_text)
                        pdf_file.close()
                        output_file.close()
                        response = response + f'SUCCESSFUL! contents read from {file} and stored in output.txt'
            else:
                return 'OUTPUT File doesnt exist'
    else:
        return 'CONTENT Folder doesnt exist'
    return response
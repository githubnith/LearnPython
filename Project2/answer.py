import PyPDF2, os
from PyPDF2 import PdfFileReader


if os.path.isdir("./content"):
    print(os.listdir('./content'))
    folders = os.listdir('./content')
    for index,folder in enumerate(folders):
        print('In DIR :')
        print(os.listdir('./content/'+ folder))
        subDir = './content/'+ folder + '/'
        files = os.listdir('./content/'+ folder)
        for file in files:
            if os.path.isfile(subDir + file) and (file).endswith('.pdf'):
                filePath = subDir + file
                print('FILE :' + filePath)
                if os.path.isfile(subDir + '/output.txt'):
                    pdf_file = open(filePath,'rb')
                    output_file=open(subDir + '/output.txt','w+')
                    pdf_reader = PyPDF2.PdfReader(pdf_file)
                    
                    print('Number of pages ' + str(len(pdf_reader.pages)))
                    for page in range(len(pdf_reader.pages)):
                        page = pdf_reader.pages[page]
                        page_text = page.extract_text()
                        output_file.writelines(page_text)
                    pdf_file.close()
                    output_file.close()
                    print('SUCCESSFUL! contents read from testfile.pdf and stored in output.txt')
                else:
                    print('OUTPUT File doesnt exist')
            else:
                print('TEST PDF File doesnt exist')
else:
    print('CONTENT Folder doesnt exist')
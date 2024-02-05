import PyPDF2, os
from PyPDF2 import PdfFileReader

def project2():
    response = ''
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
                        response = response + f'SUCCESSFUL! contents read from {file} and stored in output.txt'
                    else:
                        return 'OUTPUT File doesnt exist'
                else:
                    continue
    else:
        return 'CONTENT Folder doesnt exist'
    return response
import PyPDF2, os, re
from PyPDF2 import PdfFileReader
from configparser import ConfigParser 

if os.path.isdir("./content"):
    if os.path.isfile('./content/testfile.pdf'):
        if os.path.isfile('./content/output.txt'):
            f = open('./content/testfile2.pdf','rb')
            file1=open('./content/output.txt','w+')
            pdf_reader = PyPDF2.PdfReader(f)
            print('Number of pages ' + str(len(pdf_reader.pages)))
            print('Enter a page number :')
            page_num = int(input())
            page = pdf_reader.pages[page_num-1]
            page_text = page.extract_text()
            #print(page_text)

            configur = ConfigParser() 
            #If a file named in filenames cannot be opened, that file will be ignored.
            print(configur.read('config.ini')) 
            try:
                print ("Pattern in config: ", str(configur.get('pattern','regex')))
                pattern = r"{}".format(configur.get('pattern', 'regex'))
            except:
                print ("Section in config file NOT FOUND")
            else: 
                print (f"Pattern in string: {pattern}")
                res_search = re.findall('Aenean pulvinar', page_text)
                # this doesnt work
                # res_search = re.findall(pattern, page_text)
                for match in re.finditer(pattern, page_text):
                     print(f"Match: {match.group()}")
                # this WORKS
                print(res_search)
                print(f"Matches: {res_search}")
                file1.writelines(str(res_search))
                f.close()
                file1.close()
                print('SUCCESSFUL! contents read from testfile.pdf and stored in output.txt')
        else:
            print('OUTPUT File doesnt exist')
    else:
        print('TEST File doesnt exist')
else:
    print('CONTENT Folder doesnt exist')
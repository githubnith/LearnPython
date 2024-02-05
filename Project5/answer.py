import PyPDF2, os, re
from PyPDF2 import PdfFileReader
from configparser import ConfigParser 
from pymongo import MongoClient 

client = MongoClient("mongodb://localhost:27017/") 
database = client.LearnPython
collection = database.questions

def connectDB(databaseName):
    cursor = collection.find() 
    for record in cursor: 
        print(record)


def extractPDFContent():
    if os.path.isdir("./content"):
        if os.path.isfile('./content/questions.pdf'):
            if os.path.isfile('./content/output.txt'):
                questionFile = open('./content/questions.pdf','rb')
                file1=open('./content/output.txt','w+')
                pdf_reader = PyPDF2.PdfReader(questionFile)
                print('Number of pages ' + str(len(pdf_reader.pages)))
                print('Enter a page number :')
                page_num = int(input())
                try:
                    page = pdf_reader.pages[page_num-1]
                except:
                    print('Cant get page number')
                else:
                    page_text = page.extract_text()
                    print(page_text)

                    configur = ConfigParser() 
                    #If a file named in filenames cannot be opened, that file will be ignored.
                    print(configur.read('config.ini')) 
                    try:
                        print ("Pattern : ", str(configur.get('pattern','regex')))
                        pattern = str(configur.get('pattern','regex'))
                    except:
                        print ("Section in config file NOT FOUND")
                    else: 
                        print ("Pattern in string: "+ pattern)
                    matches = re.finditer('Question', page_text)
                    for match in matches:
                        start = max(0, match.start() - 3)
                        end = match.end()
                        lines_above = page_text[start:end].split('\n')

                        # Insert into MongoDB
                        entry = {
                            'subject_name': subject_name,
                            'question_text': question_text,
                            'answer_options': answer_options,
                            'chapter_name': chapter_name
                        }
                        collection.insert_one(document)
                    # this doesnt work
                    #res_search = re.findall('^Question.*$', page_text)
                    # this WORKS
                        # res_search = re.findall('Question', page_text)
                        # print(res_search)
                        # file1.writelines(str(res_search))
                        # questionFile.close()
                        # file1.close()
                        # print('SUCCESSFUL! ')
            else:
                print('OUTPUT File doesnt exist')
        else:
            print('TEST File doesnt exist')
    else:
        print('CONTENT Folder doesnt exist')


# connectDB('questions') 
# extractPDFContent()
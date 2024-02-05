import fitz  # PyMuPDF
from pymongo import MongoClient

file_path = "./content/questions.pdf"  # Replace with the path to your PDF file
# Connect to MongoDB (replace the connection string with your MongoDB URI)
client = MongoClient("mongodb://localhost:27017/")
db = client["LearnPython"]
collection = db["questions"]

def extract_questions(pdf_text):
    questions = []
    lines = pdf_text.split("\n")
    
    for line in lines:
        #print(line)
        if line.startswith("Question Text"):
            question_text = line.split(":")[1].strip()
            questions.append({"Question Text": question_text})
        elif line.startswith("Answer options"):
            answer_options = line.split(":")[1].strip().split(",")
            questions[-1]["Answer Options"] = answer_options
        elif line.startswith("Chapter name"):
            chapter_name = line.split(":")[1].strip()
            questions[-1]["Chapter Name"] = chapter_name
    print(questions)
    return questions

def read_pdf(file_path):
    pdf_text = ""
    doc = fitz.open(file_path)
    
    for page_num in range(doc.page_count):
        page = doc[page_num]
        pdf_text += page.get_text("text")
    print(pdf_text)
    return pdf_text

def main():
    pdf_text = read_pdf(file_path)
    questions = extract_questions(pdf_text)

    for question in questions:
        user_input = input("Enter the Chapter Name to match: ")
        if user_input.lower() in question["Chapter Name"].lower():
            collection.insert_one(question)
            print("Match found! Entry added to MongoDB.")
        else:
            print("No match found.")

if __name__ == "__main__":
    main()
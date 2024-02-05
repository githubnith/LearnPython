from answer import extractPDFContent, connectDB

connectDB('questions')

result = extractPDFContent()

print(result)
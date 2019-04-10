import os
import re
import PyPDF2
import pytesseract
from docx import Document

def extract(data):
    ress = r'Machine Learning|machine learning|MACHINE LEARNING'
    Name = re.compile(r'Mr\.?[A-Z]\w*') #format for printing the name
    Mail = re.compile(r'[a-zA-Z0-9-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+') #format for Printing the Mail ID
    Phone = re.compile(r'(0)?(91)?\d\d\d\d\d\d\d\d\d\d') #format for Printing the Phone NO
    Skill = re.compile(r'Python|python') #format for printing the skill
    Skill2 = re.compile(ress) #format for printing the skill

    mail = Mail.finditer(data)
    phone = Phone.finditer(data)
    name = Name.finditer(data)
    skill = Skill.finditer(data)
    skill2 = Skill2.finditer(data)

    for match in name:
        res = match.group(0)
        print("Name:", res)
        new = "Name:", res
        get_data(list(new))
        
    for match in mail:
        res = match.group(0)
        print("Email ID:", res)
        new = "Email ID:", res
        get_data(list(new))
        
    for match in phone:
        res = match.group(0)
        print("Mobile No:", res)
        new = "Mobile No:", res
        get_data(list(new))
        
    for match in skill:
        res = match.group(0)
        print("Skill:", res)
        new = "Skill:", res
        get_data(list(new))
        
    for match in skill2:
        res = match.group(0)
        print("Skill:", res)
        new = "Skill:", res
        get_data(list(new))
        
    under_line()

def app(value):
    f = open("my_file.txt", "w")
    f.write(str(value))
    f.close()

file_list = []

def get_data(new):
    file_list.append(new)
    convert_str(str(file_list))

file_str = ""

def convert_str(file_list):
    value = file_str.join(file_list)
    app(value)

def under_line():
    print("___________________________________________________", sep='\n')

def txt_format(file):
    with open(file, 'r') as myfile:
        datta = myfile.read()
    data = str(datta)
    extract(data)

def pdf_format(file):
    pdf = open(file, 'rb')
    view = PyPDF2.PdfFileReader(pdf)
    page = view.numPages
    print('Number of pages: ',view.numPages)
    for i in range(0, page):
        pre = view.getPage(i)
        datta = pre.extractText()
    data = datta
    extract(data)

def docx_format(file):
    data = ""
    document = Document(file)
    for para in document.paragraphs:
        a = para.text
        data = data + a
    extract(data)

def file_formats(file):
    file_format = re.compile(r'\.[a-z]*')
    file_formats = file_format.finditer(file)
    for match in file_formats:
        res = match.group(0)
        #print("Format: ", res)
        format_file = str(res)
        #print(str(format_file))
        check_format(format_file, file)
        
def check_format(format_file, file):
    if format_file == ".txt":
        txt_format(file)
    elif format_file == ".pdf":
        pdf_format(file)
    elif format_file == ".docx":
        docx_format(file)
    
path = r"C:\Users\Deepu\Desktop\python\data\New folder\python_test\pdf"
# path = input()
def listDir(dir):
    filename = os.listdir(dir)
    for filenames in filename:
        file = os.path.abspath(os.path.join(dir, filenames))
        file_formats(file)
        

if __name__ == "__main__":
    listDir(path)
            
    

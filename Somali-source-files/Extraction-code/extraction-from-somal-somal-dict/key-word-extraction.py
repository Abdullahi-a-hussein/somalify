# import pdfplumber

from PyPDF2 import PdfReader
import os

alphabet = "abcdefghijklmnopqrstuvwxy"
alphabet_range ={char: [0, 0] for char in alphabet}

# import re
# demo = []
# with pdfplumber.open('Somali-Somali-dictionary-from-romatrepress.pdf') as pdf: 
#     first_page = pdf.pages[24]
#     #print(first_page.chars[10])
#     # print(first_page.extract_words()[-2])


reader = PdfReader("Somali-Somali-dictionary-from-romatrepress.pdf")

def letter(start_index, end_index):
    container = ""
    for index in range(start_index, end_index):
        page = reader.pages[index]
        text = page.extract_text()
        container  += container + text + "\n"
        
    return container

def write_to_raw_file(starting, ending, char):
    path = "./" + char + "-raw.txt"
    file = char + "-raw.txt"
    if os.path.exists(path):
        with open(file, "a") as raw_file:
             raw_file.write(letter(starting, ending))
    else:
        with open(file, 'w') as raw_file:
            raw_file.write(letter(starting, ending))
    print("added pages: " + str(starting) + " " + str(ending))
    

# write_to_raw_file(909, 916, 'y')
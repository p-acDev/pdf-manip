import PyPDF2
from pdf2image import convert_from_path
import pytesseract
import re
import streamlit as st

def extract_text_from_pdf_simple(filename):

    with open(filename, 'rb') as pdf_file:
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        data = data = {i: read_pdf.getPage(i).extractText() for i, page in enumerate(read_pdf.pages)}

    return data

def extract_text_from_pdf_ocr(filename):

    # first transform pdf to image for image recognition
    page_images = convert_from_path(filename)
    
    data = {i: str(((pytesseract.image_to_string(image)))) for i, image in enumerate(page_images)}

    return data

def write_output(data, targets):

    output = ""

    output += "numero page,nombre d'occurences\n\n"

    for target in targets:
        output += f"target: {target}\n######\n"
        for page_number in data.keys():
            output += f"{page_number + 1},{len([_ for _ in re.finditer(target, data[page_number], re.IGNORECASE)])}\n"
        output += "\n"

    return output

def gui():

    st.write("# PDF sniffer")

    pdf_file = st.file_uploader("Chargez votre pdf")

    pdf_type = st.radio("Selectionnez votre type de pdf",
        ('Saisie de texte impossible', 'Saisie de texte possible'))

    targets = st.text_input("Entrez vos recherches séparées par des ','")

    if targets is not None:
        targets = targets.split(',')
    
    if st.button("Lancer la recherche") and pdf_file is not None and targets is not None:
        with st.spinner("Wait for it ..."):

            if pdf_type == 'Saisie de texte possible':
                data = extract_text_from_pdf_simple(pdf_file.name)
            else:
                data = extract_text_from_pdf_ocr(pdf_file.name)
            output = write_output(data, targets)

            st.success("Recherche terminée")
            st.text(output)
    
    return None

if __name__ == "__main__":

    gui()
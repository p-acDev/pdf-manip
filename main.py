import PyPDF2
from pikepdf import Pdf
from pdf2image import convert_from_path, convert_from_bytes
import pytesseract
import re
import streamlit as st
import pandas as pd
import json

def merge(pdfs):
    
    # buil an empty pdf
    fusion = Pdf.new()

    # loop over each pdf
    for _pdf in pdfs:
        src = Pdf.open(_pdf)
        # add all pages of the open pdf to the new created pdf 
        fusion.pages.extend(src.pages)
    
    return fusion

def extract_text_from_pdf_simple(filename):

    with open(filename, 'rb') as pdf_file:
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        data = data = {i: read_pdf.getPage(i).extractText() for i, page in enumerate(read_pdf.pages)}

    return data

def extract_text_from_pdf_ocr(binary):

    # first transform pdf to image for image recognition
    page_images = convert_from_bytes(binary)
    
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

    st.write("# Outils pour manipuler les pdf")

    choice = st.sidebar.selectbox("Selectionner votre besoin",
    ("-", "fusion", "extraction de texte"))

    if choice == "extraction de texte":

        st.write("# PDF sniffer")

        pdf_file = st.file_uploader("Chargez votre pdf")
        
        if pdf_file is not None:
            binary = pdf_file.getvalue()
        

        operation_choice = st.selectbox("Que voulez faire ?",
        ("-", "Trouver des occurences de mots", "extraire tout le texte"))

        if operation_choice == "Trouver des occurences de mots":

            targets = st.text_input("Entrez vos recherches séparées par des ','")

            if targets is not None:
                targets = targets.split(',')
            
            if st.button("Lancer la recherche") and pdf_file is not None and targets is not None:
                with st.spinner("Wait for it ..."):
                    data = extract_text_from_pdf_ocr(binary)

                    output = write_output(data, targets)

                    st.success("Recherche terminée")
                    st.text(output)

        elif operation_choice == "extraire tout le texte":
            if st.button("Extraire") and pdf_file is not None:
                with st.spinner("Wait for it ..."):
                    data = extract_text_from_pdf_ocr(binary)
                    text_data = json.dumps(data)
                    st.success("Extraction terminée")
                    st.download_button("Télécharger", data=text_data)

    elif choice == "fusion":
        st.write("# pdf-fusion")

        pdfs = st.file_uploader("Chargez vos fichiers pdf à fusionner", accept_multiple_files=True)

        if pdfs is not None:

            if st.button("Fusionner"):

                fusion = merge(pdfs)
                fusion.save("fusion.pdf")
                st.success("PDF fusionné")

                with open("fusion.pdf", 'rb') as f:
                    PDFbyte = f.read()

                st.download_button(label="download",
                data=PDFbyte,
                file_name="fusion.pdf",
                mime='application/octet-stream')
                


    return None

if __name__ == "__main__":

    gui()
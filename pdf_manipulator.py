import sys
from time import sleep
import os
import sys
from pikepdf import Pdf
import version
from urllib.parse import quote

def merge(pdfs):
    
    # buil an empty pdf
    pdf = Pdf.new()

    # loop over each pdf
    for _pdf in pdfs:
        src = Pdf.open(_pdf)
        # add all pages of the open pdf to the new created pdf 
        pdf.pages.extend(src.pages)
        #pdf.save('merged.pdf')
    
    return pdf

def preview(pdf_name):
    
    if pdf_name != "":
        # put in universal format for path 
        pdf_name = pdf_name.replace('\\', '/')
        
        # in case spaces in name we nee dto encode them so that brower does not 
        # split tthe url into several url
        url = "file:///{}".format(quote(pdf_name, safe=":/")) 
        
        os.system("start chrome {}".format(url))

    return pdf_name

def remove_pages(pdf_name, pages):

    pdf = Pdf.open(pdf_name)
    pages_to_be_removed = []
    print(pages)
    print(pdf_name)

    for p in pages.split(','):
        if "-" in p:
            for i in range(int(p.split("-")[0]), int(p.split("-")[1]) + 1):
                pages_to_be_removed.append(i)
        else:
            pages_to_be_removed.append(int(p))

    k = 0
    for p in pages_to_be_removed:

        del pdf.pages[p - 1 - k]
        k += 1

    pdf.save(pdf_name[:-4] + "_pages_removed.pdf")


    return None

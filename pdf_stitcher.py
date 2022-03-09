from PyPDF2 import PdfFileMerger
import os
import glob

directory = os.path.abspath(
    "E:\\OneDrive\\Uni Work\\Algorithms Data Structures and Programming\\week3\\pdfs\\"
)

filetype = "*.pdf"
output_filename = "week3_all_files.pdf"

list_of_files = [file for file in glob.glob(os.path.join(directory, filetype))]

# https://stackoverflow.com/questions/3444645/merge-pdf-files
merger = PdfFileMerger()

for file in list_of_files:
    merger.append(file)

merger.write(os.path.join(directory, output_filename))

merger.close()

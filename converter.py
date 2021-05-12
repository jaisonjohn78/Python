#importing modules
from pdf2image import convert_from_path
from tkinter import *


# Store Pdf with convert_from_path function
images = convert_from_path('sample.pdf', dpi=400)        #name of the pdf

#use the following inside convert_from_path('sample.pdf') to change settings..
#(pdf_path, dpi=200, output_folder=None, first_page=None, last_page=None, fmt="ppm", jpegopt=None, thread_count=1, userpw=None, use_cropbox=False, strict=False, transparent=False, single_file=False, output_file=uuid_generator(), poppler_path=None, grayscale=False, size=None, paths_only=False, use_pdftocairo=False, timeout=None)


for i in range(len(images)):
	# Save pages as images in the pdf
	images[i].save('page'+ str(i) +'.jpg', 'JPEG')
import PyPDF2

import sys

inputs = sys.argv[1:] #will call all except first, so we can add as many pdf as we want

def pdf_combiner(pdf_list):
  for pdf in pdf_list:
    print(pdf)

pdf_combiner(inputs)

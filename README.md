# Bank_statement_parsing

## Overview

This script extracts data from bank statement PDFs. It performs the following tasks:

1. Extracts data from PDF.
2. Pre-processes the extracted data to remove extra columns, align columns, and clean up the data.
3. Saves the processed data into an Excel file.

## Requirements

You need have python 3.8 to run this on your system.

You can install the required packages after installing python using the following command:

### pip install -r requirements.txt

## How to Run
Place your PDF bank statement file in the desired directory.

Update the path to the PDF file in the script:

### pdf_path = r'D:\Invoices_parsing\standard-bank-3.pdf'

Run the script:

### python your_script_name.py


The output will be saved as an Excel file in the same directory as the PDF, with the same name but with an .xlsx extension.

## Tested on python 3.8

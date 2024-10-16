import camelot
import pandas as pd
import re

def pre_processing(df):
    header_list = ['Details', 'Service Fee', 'Debits', 'Credits', 'Date', 'Balance']
    # Check if the number of columns is 7
    if len(df.columns) == 7:
        # Remove the second column (index 1) entirely
        df = df.drop(df.columns[1], axis=1)


    # Find the row where the first column contains "BALANCE BROUGHT FORWARD"
    balance_start_idx = df[df[0].str.contains('BALANCE BROUGHT FORWARD', na=False)].index
    if len(balance_start_idx) > 0:
        # Set the DataFrame to start from this row (dropping any rows before)
        df = df.loc[balance_start_idx[0]:].reset_index(drop=True)
        #set the header using the static list of strings
        df.columns = header_list


    for i in range(len(df)):
        row = df.iloc[i]
        # Check if there is a space or newline in the third column
        if isinstance(row[2], str) and (' ' in row[2] or '\n' in row[2]):
            # Split by space or newline, and move the value before the space/newline to the second column
            parts = re.split(r'[\s\n]+', row[2], maxsplit=1)
            if len(parts) > 1:
                df.iloc[i, 1] = parts[0]  # Move the first part to the second column
                df.iloc[i, 2] = parts[1]  # Keep the remaining part in the third column
    return df





def extraction(pdf_file):

    print('Extracting Data')
    tables=camelot.read_pdf(pdf_file,flavor='stream')
    table_detected=False
    if len(tables)==1:
        table_detected=True
        df=tables[0].df
    elif len(tables)>1:
        table_detected=True
        df=tables[-1].df
    else:
        df=pd.DataFrame()
    if not table_detected:
        print('Data is Empty')
    else:
        print('Processing data')
        df=pre_processing(df)
        output_file=pdf_file.replace('.pdf', '.xlsx')
        df.to_excel(output_file,index=False)





pdf_path=r'D:\Invoices_parsing\standard-bank-3.pdf'
extraction(pdf_path)


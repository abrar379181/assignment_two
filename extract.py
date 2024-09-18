import pandas as pd
import os

def extract_text_from_csv(csv_files, text_column, output_file):
    with open(output_file, 'w') as outfile:
        for file in csv_files:
            df = pd.read_csv(file)
            print(f"Processing file: {file}")  # Print to confirm processing
            if text_column in df.columns:
                texts = df[text_column].tolist()
                for text in texts:
                    outfile.write(text + '\n')
            else:
                print(f"Column '{text_column}' not found in {file}")  # Print if column is missing


csv_files = ['CSV1.csv', 'CSV2.csv', 'CSV3.csv', 'CSV4.csv']
output_file = 'combined_text.txt'


extract_text_from_csv(csv_files, 'TEXT', output_file)


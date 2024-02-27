# Certo2YNAB
A python script to extract the transaction data from the Cembra Certo monthly statement PDF.

This is a very quick and dirty python script to extract the transaction data from the Cembra Certo monthly statement PDF to CSV. The CSV is optimized for import into YNAB (You Need A Budget), but it can probably be used with other personal finance software tools.
I am using [pypdf](https://github.com/py-pdf/pypdf) to extract the text from the PDF.

## Usage
Make sure to have python3 installed on your system:
```bash
python3 --version
```

install pypdf:
```bash
python3 -m pip install pypdf
```

run the script; replace INPUT with the filename of your PDf; replace OUTPUT with the desired filename of the CSV:
```bash
python3 certo2ynab.py "INPUT.pdf" "OUTPUT.csv"
```

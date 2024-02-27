from pypdf import PdfReader
import re
import sys

def starts_with_date(s):
    # Regular expression for matching DD.MM.YYYY format
    # pattern = r'^\d{2}\.\d{2}\.\d{4}'
    pattern = r'^\d{2}\.\d{2}\.\d{4} \d{2}\.\d{2}\.\d{4}'
    return re.match(pattern, s) is not None

pdf_file = sys.argv[1]
csv_file = sys.argv[2]

f = open(csv_file, "a")

reader = PdfReader(pdf_file)
text = ""
for page in reader.pages:
        text += page.extract_text() + "\n"

header_line = "Date	Date del	Payee	Outflow	Inflow"
print(header_line)
f.write(header_line + "\n")

for line in text.splitlines():
    if starts_with_date(line) == True:
        s = line
        parts = s.split(' ', 2)
        last_part_split = parts[-1].rsplit(' ', 1)
        result = parts[0] + '\t' + parts[1] + '\t' + last_part_split[0] + '\t' + last_part_split[1]
        print(result)
        f.write(result + "\n")

f.close()


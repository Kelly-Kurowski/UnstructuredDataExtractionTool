from pdfminer.high_level import extract_text

pdf_path = r"C:\Users\kelly\OneDrive\Bureaublad\Inkoop Facturen labSC\13593-4137-bro-2023.pdf"

text = extract_text(pdf_path)
print(text)
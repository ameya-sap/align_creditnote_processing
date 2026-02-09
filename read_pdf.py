import sys
import pypdf

reader = pypdf.PdfReader('/Users/ameyaps/Documents/prototypes/align_creditnote_processing/TDD_ AI-Powered Credit Note Processing.pdf')
text = ""
for i, page in enumerate(reader.pages):
    print(f"--- Page {i+1} ---")
    print(page.extract_text())

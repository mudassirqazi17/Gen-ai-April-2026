import PyPDF2, docx

def extract_text(file):
    name=file.name.lower()
    if name.endswith('.pdf'):
        reader=PyPDF2.PdfReader(file)
        return '\n'.join([p.extract_text() or '' for p in reader.pages])
    if name.endswith('.docx'):
        d=docx.Document(file)
        return '\n'.join([p.text for p in d.paragraphs])
    return file.read().decode('utf-8', errors='ignore')

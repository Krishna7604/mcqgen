import PyPDF2
def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pagereader=PyPDF2.PdfReader(file)
            text=""
            for page in pagereader.pages:
                text+=page.extract_text()
            return text
        except Exception as e:
            raise Exception("Error in opening the file")
    elif file.name.endswith(".txt"):
        return file.read().encode("utf-8")
    else:
        raise Exception("Error occured in opening tht file")

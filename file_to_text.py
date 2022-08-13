import PyPDF2

class FileToText:
    def pdf_to_text(file_path):
        pdf_file_object = open(file_path, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file_object)

        page_object = pdf_reader.getPage(16)
        pdf_text = page_object.extractText()

        pdf_file_object.close()

        return pdf_text
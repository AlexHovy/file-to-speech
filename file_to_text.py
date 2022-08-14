import PyPDF2

class FileToText:
    def __init__(self, file_path):
        self.file_path = file_path

        pdf_file_object = open(file_path, 'rb')
        self.pdf_reader = PyPDF2.PdfFileReader(pdf_file_object)
        
    @property
    def page_count(self):
        return self.pdf_reader.numPages

    def get_text_by_index(self, index):
        page_object = self.pdf_reader.getPage(index)
        pdf_text = page_object.extractText()
        return pdf_text
    
    def close(self):
        self.pdf_file_object.close()
import pdfkit
import threading

def convert_to_pdf(url, file_name, config):
    pdfkit.from_url(url, file_name, configuration=config)

path_wkh = r'C:\Users\Mubina\Documents\python 5\Exam5\task-2\omonims'

config  = pdfkit.configuration(wkhtmltopdf=path_wkh)

threads = []

for i in range(1, 11):
    url = f'https://tilshunos.com/omonims/?page={i}'
    pdf_filename = str(i) + '.pdf'
    thread = threading.Thread(target=convert_to_pdf, args=(url,pdf_filename, config))

    thread.append(thread)
    thread.start()

for thread in threads:
    thread.join()

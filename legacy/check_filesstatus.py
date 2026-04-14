import psutil  # for accessing the process utilities  !
from urllib.request import urlopen  # If there is a webpage to be downloaded
from pdfminer.pdfinterp import PDFResourceManager, \
    process_pdf  # For creating the resource manager and processor for the pdf
from pdfminer.converter import TextConverter  # For the conversion of the Text in the pdf
from pdfminer.layout import LAParams  # Taking the Linear layout in mind
from io import StringIO  # String IO for conversion to string representation


def get_all_running_files():
    file_list = []  # This gets the list of the files
    for proc in psutil.process_iter():  # going through all of the processes to get the list of the running processes
        try:
            if len(proc.open_files()) != 0:  # If there is a process running
                file_list.append(proc.open_files())  # adding in the file so that the data can be used.
        except:
            continue
    return file_list  # this returns the file list


def get_pdf_files(file_list=get_all_running_files()):
    pdf_files_location = []
    for list in file_list:
        for inner_list in list:
            if str(inner_list).split(',')[0].__contains__('.pdf'):  # Splitting on the basis of commas as it will be providing the data !
                if str(inner_list).split(',')[0][16:-1].endswith('StandardBusiness.pdf'):
                    continue
                else:
                    pdf_files_location.append(str(inner_list).split(',')[0][16:-1]) # this wil get the file location

    return pdf_files_location  # Returns the list for the pdf file location !
    # print(pdf_file_list)

def readPDF( pdfFile):
    try:
        rsrcmgr = PDFResourceManager()  # Creates the resource manager
        # resource_mang = PDFResourceManager()
        retstr = StringIO()  # string object for the representation of the pdf
        # string represetnation from string input and output module
        laparams = LAParams()  # Parameters Object Creation
        device = TextConverter(rsrcmgr, retstr, laparams=laparams)  # Creating the device for the conversion
        process_pdf(rsrcmgr, device, pdfFile)  # Process the specific pdf, to convert into string representations
        device.close()  # Closes the device.
        # print(retstr) # Debuggin
        # Decoded value is returned here UTF-8
        content = retstr.getvalue()  # gets the text from the string object
        # print(content)5
        return content  # Returns the content where its called
    except Exception as Ex:
        print("While reading the file , there was an error in the function Readodf as :", Ex)
        # printing the exception
def filter_data(data_value):
    data_value = str(data_value).replace("\\\\\\\\", "/")
    return data_value


#
def test():
    # K = get_all_running_files()
    # for i in K:
    #     print(i)
    K = get_pdf_files()
    K = filter_data(K[0])  # Filtering the data for the K
    file_read = open(K, "rb")
    data = readPDF(file_read)
    new_data = ""

test()
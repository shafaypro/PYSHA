from urllib.request import urlopen  # If there is a webpage to be downloaded
from pdfminer.pdfinterp import PDFResourceManager, \
    process_pdf  # For creating the resource manager and processor for the pdf
from pdfminer.converter import TextConverter  # For the conversion of the Text in the pdf
from pdfminer.layout import LAParams  # Taking the Linear layout in mind
# import BytesIO
from io import StringIO  # String IO for conversion to string representation
from io import open  # opening the file
from zipfile import ZipFile  # Zip file will be used to zip word into xml
from io import BytesIO  # for the conversion of the word files will be used later
import os  # the module will be used to find in the correct directory and files extensions check
import docx  # importing the docs module as per advised
import ntpath  # for extracting filename from full path

try:
    import pyPDF2  # another module for conversion of text
except Exception:
    pass


class FilestoTextFiles:
    dir_path = os.path.dirname(os.path.realpath(__file__))  # Global Object accessible directory name

    # Constructor aka INITIALIZER
    def __init__(self):
        print("FilestoTextFiles have been intialized")  # Debugging

    # The below function writes to a file_name as .txt extension, for later onward.
    def save_to_txt(self, text_data, file_name):
        file_name = ((file_name.replace(".pdf", ".txt")).replace(".docx", ".txt")).replace(".doc",
                                                                                           ".txt")  # Renaming the file to txt
        exact_path = ntpath.basename(file_name)
        # if not os.path.exists(self.dir_path+"\\ConvertedTexts"):
        #     os.makedirs(self.dir_path+"\\ConvertedTexts")
        # file_writer = open(self.dir_path+"\\ConvertedTexts\\"+str(file_name), "w")  # Writing option in the file
        if not os.path.exists(self.dir_path + "/ConvertedTexts"):
            os.makedirs(self.dir_path + "/ConvertedTexts")
        file_writer = open(self.dir_path + "/ConvertedTexts/" + exact_path, "w")  # Writing option in the file
        # file_writer = open(file_name, "w")  # Writing option in the file
        # print(text_data.encode('utf-8'))
        file_writer.writelines(str(text_data.encode('utf-8')))  # Writes to a file
        file_writer.close()  # Closes the file writer.

    # The below function is responsible for the reading of the pdf File
    def readPDF(self, pdfFile):
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
            print("While reading the file , there was an error in the function Readodf as :",
                  Ex)  # printing the exception

    # Check case for the pdf
    def testpdf(self):
        try:
            pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")  # Gettting from the web
            print("Converting ...")
            # print(pdfFile)
            outputString = self.readPDF(pdfFile)  # Calls the function to read from the pdf
            # pdfFile.close() # Closes the pdf File
            print("Conversion Completed")  # Debugging
            return outputString  # this returns the output string for the specified format
        except Exception as Ex:
            print("Unable to convert the pdf to text due to : ", Ex)  # Printing the Exception
            # print(Ex)  # DEBUGGING
            print("In function testpdf")  # Testing
        finally:
            pdfFile.close()  # keep in mind to close the file which you are working on !

    # Converting the specified file to pdf

    def convert_pdf(self, pdf_filelocation):
        if pdf_filelocation != "":
            print(pdf_filelocation)
            pdf_File = open(pdf_filelocation, "rb")  # Opens the pdf in the read format
            print("Converting ..")  # PROMPT
            outputString = self.readPDF(pdf_File)  # Calls the read PDF function to work on with it
            lines = outputString.split("\n")
            outputvalue = ""
            for line in lines:  # Since the line contains the next line and the unicode schemes to remove those.
                if line != "":
                    line = line.strip()
                    line = line.replace("b\"", "")  # replacing for the filtering
                    outputvalue += line  # Adding in the output value again and again.
            return outputvalue  # Returns the output string to the function called
        else:
            print('There is no Location Valid , specified ')  # DEBUGGING
            # pdf_File.close() # Closes the specified file

    # The below function recieves the list of pdf files and then convert them in to set of files.

    def convert_list_pdffiles(self, list_pdfs):
        # total_file_text_data = []  # This is the list storing the file information as specified
        if len(list_pdfs) >= 1 and type(list_pdfs) == list:
            for filelocation in list_pdfs:
                # file_data = open(filelocation, "rb")  # reading the specifid file
                text_converted_file = self.convert_pdf(filelocation)  # Converts the file data to the text format
                # The below function writes to txt
                file_name = filelocation.split("\\")[-1]  # Gets the file name from the speified path
                print("Converted -->" + file_name)
                self.save_to_txt(text_converted_file, file_name)  # --Saving to .txt file
                # total_file_text_data.append(total_file_text_data)  # Appends in the list of the text files
                # return total_file_text_data # returns to the main function the total file text data with multiple files in action
            print("All the pdf files have been converted")  # PROMPT
        else:
            print(
                "List of pdf files had length less equal toone and the type pf the files passed are not in the form of list")  # DEbugging

    def get_AllpdfFiles(self):
        # Get all the PDF filenames.
        pdfFiles = []  # this is the pdf file list
        # for filename in os.listdir(self.dir_path + "\\Files"):  # Specifying the folder and looping through the folder
        for filename in os.listdir(self.dir_path + "/Files"):  # Specifying the folder and looping through the folder
            if filename.endswith('.pdf'):
                # pdfFiles.append(self.dir_path + "\\Files\\" + filename)  # Adding the pdf complete location in the list.
                pdfFiles.append(self.dir_path + "/Files/" + filename)  # Adding the pdf complete location in the list.
        pdfFiles.sort(key=str.lower)
        return pdfFiles

    '''----BELOW FUNCTIONS ARE FOR WORD FILES with .doc or .docx---'''

    def read_wordFile(self, filename):  # Reading the file from the word file
        doc = docx.Document(filename)  # Creating the document of docs form the specified fule
        fullText = []  # Creating a list of texts
        for para in doc.paragraphs:
            fullText.append(para.text)
        return '\n'.join(fullText)  # returning by joining in the next line by line

    def get_AllwordFiles(self):
        wordFiles = []  # List which wil be holding the file names of word file
        # for filename in os.listdir(self.dir_path + "\\Files"):  # listing the current directory files
        for filename in os.listdir(self.dir_path + "/Files"):  # listing the current directory files
            if filename.endswith('.word') or filename.endswith('.docx') or filename.endswith('.doc'):
                # wordFiles.append(self.dir_path + "\\Files\\" + filename)  # adds the file name in the word list
                wordFiles.append(self.dir_path + "/Files/" + filename)  # adds the file name in the word list
        wordFiles.sort(key=str.lower)  # sorts the list with respect to key value
        return wordFiles  # returns all the file list

    def convert_allwordFiles(self, wordfilelist):
        if type(wordfilelist) == list and len(wordfilelist) >= 1:
            for single_wordFile in wordfilelist:
                data = self.read_wordFile(single_wordFile)  # Calling in the word data writing function
                file_name = single_wordFile.split("\\")[-1]  # Gets the file name from the speified path
                lines = data.split("\n")
                total_data = ""  # Will hold the data
                for line in lines:  # Data filterning
                    if line != "":
                        line = line.strip()
                        total_data += line + "\n"  # Appending in the line
                print("Converting...." + single_wordFile)
                self.save_to_txt(total_data, file_name)  # Passing the data and the single file name to the list
        else:
            print("NOPE NOT POSSIBLE")

    def convert_all(self):
        pdf_files = self.get_AllpdfFiles()  # Gets all the pdf file.
        word_files = self.get_AllwordFiles()  # Gets all the word files.
        print("pdf Files found are ", pdf_files)  # Prompting the message in the console
        print("word_files found are", word_files)  # prompting the message on console
        '''----------------READING AND CONVERTING ALL THE PDF FILES TO TXT FILES -------------------------------'''
        self.convert_list_pdffiles(pdf_files)  # Calls in the convert function to convert all the pdfs
        self.convert_allwordFiles(word_files)  # Converts all the word files
        # pdf_files_converted_data = self.convert_list_pdffiles(pdf_files)  # Gets all the data in the pdf files .
        # The Above returns a list .


import sqlite3

class db_data:
    # setting the connection to None and the Cursor to none
    connection = None
    cur = None
    # this is the intializer for the constructor
    # intializing the database
    def __init__(self):
        print("This is the Instantiation Function of the Class dbdata")
        self.connection = sqlite3.connect("Localdb/DBPYSHA.sqlite3")  # Creating the SQLITE3 database PYSHA
        self.cur = self.connection.cursor()  # Creting the cursor for the attachment of the database
        try: # if the database doen't exists than create the database
            self.create_database()
            # Trying to create the database for th create_Database()
        except Exception as E:  # if id does prints the exception and then let it rock
            print("Database already exists",str(E))
    def create_database(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Requests(r_id INTEGER PRIMARY KEY AUTOINCREMENT,r_text TEXT,r_responce TEXT)''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Reminders(Rem_id INTEGER  PRIMARY KEY AUTOINCREMENT,Rem_name TEXT,Rem_Date Date)''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS HISTORY(H_id INTEGER PRIMARY KEY AUTOINCREMENT, H_request_Text TEXT,H_Date Date DEFAULT CURRENT_TIMESTAMP)''')
    # REQUESTS Table Modifications

    def insert_into_Requests(self,r_Text,r_Responce):
        self.cur.execute('''INSERT INTO Requests(r_Text,r_responce) VALUES (?,?)''', (r_Text,r_Responce))
        self.connection.commit()  # this commits all the changes
        return
    # inserting in to history of the database
    def insert_into_History(self,h_text):
        self.cur.execute('''INSERT INTO HISTORY(H_request_Text) VALUES (?)''',(h_text,)) # inserting the tupple in the database
        self.connection.commit() # commits all the changes
        return
    # if you want to search in the history and get the data
    def search_in_History(self,h_text_search):
        self.cur.execute('''Select H_id,H_Date from HISTORY where H_request_Text = ?''',(h_text_search,)) # inserting the tupple in the database
        returned_text = self.cur.fetchall() # gets the returned data from the H_id
        self.connection.commit() # commits all the changes
        return returned_text

    # Find the request in the database , if already exists then add otherwise renew
    def search_into_Requests(self,r_text):
        self.cur.execute('''Select r_Responce from Requests where r_Text=?''',(r_text,))
        result = self.cur.fetchall()
        self.connection.commit() # this commits all the database
        return result # this returns the searched text back
    # delete all the data fort the table
    def delete_all(self):
        self.cur.execute('''DROP TABLE Requests''')
        self.cur.execute('''DROP TABLE Reminders''')
        self.cur.execute('''DROP TABLE HISTORY''')
        self.connection.commit() # commiting the database
        return
    # Connecting to the database for the current data
    def connect_database(self,db_file):
        if str(db_file).endswith(".sqlite3"):
            self.connection = sqlite3.connect(db_file) # connecting to the database filename
            cur = self.connection.cursor()
        else:
            print("Desired database required, invalid file name")
    # inserting the dummy data in the database
    def dummy_insert(self):
        self.cur.execute('''INSERT INTO Requests(r_Text,r_responce) VALUES ('who are you','I am PYSHA you personal assistant')''')
        self.connection.commit() # this runs the query above
    # reforming the output , exlucding the extra key words in the data string
    def reform_output(self,input_in):
        input_in = str(input_in).replace('[', '')
        input_in = input_in.replace(']', '')
        input_in = input_in.replace("'", '')
        input_in = input_in.replace("(", '')
        input_in = input_in.replace(")", '')
        input_in = input_in.replace(",", '')
        return input_in
    # deletingthe history for the database !
    def delete_history(self):
        print("Deleting History..")
        self.cur.execute('''DELETE  FROM HISTORY''')
        self.connection.commit()
        return

    # Keep in mind to remove the below's code as it will be replaced by the __PYSHA.py files
if __name__ == '__main__':
    db = db_data()
    db.create_database()
    #db.delete_all() # this deleted all the database
    #db.dummy_insert() # just for debugginh purposes
    #returned_string = db.search_into_Requests("who are you")
    #$returned_reformed_output = db.reform_output(returned_string)
    #print(returned_reformed_output)
    db.insert_into_History("What is the basic purpose")
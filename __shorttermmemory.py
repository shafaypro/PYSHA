# TODO : Add the last 7 text inputs and the processed results for the conclusion of the text
from _dbdata import *  # importing the data from the database


def __stmcheck():
    db = db_data()  # creating the database connection
    short_term_data = list(db.short_term_check())
    for stm_m in short_term_data:   # looping through the short term memory
        print(stm_m)  # printing the short term memory
__stmcheck()  # Debuggin purpose
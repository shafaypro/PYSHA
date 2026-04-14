# TODO : Add the last 7 text inputs and the processed results for the conclusion of the text
from _dbdata import *  # importing the data from the database
import random

def stmcheck():
    db = db_data()  # creating the database connection
    short_term_data = list(db.short_term_check())
    return short_term_data  # just for debugging purpose


def filter_stm_sentences(partial_sentence=""):
    partial_sentence = str(partial_sentence).replace("('", "")
    partial_sentence = partial_sentence.replace("',)", "")
    return partial_sentence  # returning the partial sentence


def display_stm(short_term_data):  # Expected a list so that it might be displayed
    final_generated_shorttermlist = []
    for stm_m in short_term_data:  # looping through the short term memory
        final_generated_shorttermlist.append(filter_stm_sentences(stm_m))  # printing the short term memory
    return final_generated_shorttermlist


'''Below is the sample code to run to check this particular module to start working with'''
# check = stmcheck()  # Debuggin purpose
# # print(display_stm(check))
# stm_list_recieved = stmcheck()  # calls the stm check module
# list_recieved = display_stm(stm_list_recieved)  # Filterening all the sentences and specifying the current list
# print(list_recieved)
# random.shuffle(list_recieved)
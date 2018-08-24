import os
import time


class MUSIC_PLAYER:
    music_list = list()  # list creation
    current_music = ""  # This wil have the current music
    position = 0

    def __init__(self):
        self.music_list = self.get_all_music()
        #print(self.music_list)

    # Getting the list of all the music
    def get_all_music(self):
        for filename in os.listdir("E:\MusicVideos"):  # Specifying the folder and looping through the folder
            if filename.endswith('.mp4'):  # Ending it with the mp4
                # pdfFiles.append(self.dir_path + "\\Files\\" + filename)  # Adding the pdf complete location in the list.
                self.music_list.append("E:\MusicVideos\\" + filename)  # Adding the mp4 file name addition ,
        self.music_list.sort(key=str.lower)  # sorting the Music player
        return self.music_list  # Returning to the main function.

    # Getting the current soundtrack
    def current_music(self):
        if len(self.music_list) > 1:
            print(self.music_list[self.position])  # This prints out the specific music
        else:
            print("No music found")  # There is no music found

    # Getting the next music in the particular directory from the list
    def next_music(self):
        if self.position + 1 < len(self.music_list):
            # Checking if the position of the Specific is less than the other one
            self.position += 1
            # print(self.music_list[self.position])  # Prints out the current list of the music player
            return self.music_list[
                self.position]  # Returned the music from the specified music list and the position of the list
        else:
            return self.music_list[self.position]  # returns the music value

    # Getting the previous music in the items of the list ...
    def previous_music(self):
        if self.position - 1 >= 0 and len(self.music_list) > 1:  # Two condition checking for the specified list
            self.position -= 1
            # print(self.music_list[self.position])
            return self.music_list[self.position]  # Returns to the called function
        else:
            return self.music_list[self.position]  # Returns the default music element to the called funciton

    def play_music_video_file(self, locationfile):
        try:
            print("start  " + locationfile)
            os.system("start  " + locationfile)  # This will start the particular music
        except Exception as Ex:
            print("check the directory exception", Ex)

    # --Control the particular player--#


    def control_player(self, command=""):
        if command == "":
            return None
        else:
            if command == "next music":
                music_loc = self.next_music()
                print("----->", music_loc)
                self.play_music_video_file(music_loc)
                # this returns the next music location
            elif command == "previous music":
                music_loc = self.previous_music()  # previous
                print("-----<", music_loc)
                self.play_music_video_file(music_loc)  # This returns the Previous music
            elif command == "current music":
                self.play_music_video_file(self.current_music())  # This returns the current music

                # TO DO ; The spaces product an error while running though the assistant so
                # You have to work


# -- Below is the test function
#
#
# def test():
#     ms = MUSIC_PLAYER()  # The Object of the music player class has been createdh
#
#     # Music player class is being created
#     # music name = ms.next_music()  # Gets the next music item
#     # This will call in the control player and then call in the next music
#     ms.control_player("next music")  # calls in the next music
#
#     # ms.control_player("next music")
#     # time.sleep(10)
#     # ms.control_player("next music")
#
#
# test()  # Testing function

# This class will be responsible for the manipulation of the images
import os  # operating system module for the file checkign
import time  # time pause for the change of thespecified image after a time interval !!!!

class IMAGE_CHECK:
    image_list = list()  # list creation
    current_image = ""  # This wil have the current music
    position = 0  # positions for the specific

    # ---------------------------------------------------------------------------- #

    def __init__(self):
        # print("Object for the image check ")
        self.image_list = self.get_images()

    def get_images(self):
        for filename in os.listdir("E:\Wallpapers"):  # Specifying the folder and looping through the folder
            if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith(
                    '.jpeg') or filename.startswith('.'):  # Ending it with the mp4
                # pdfFiles.append(self.dir_path + "\\Files\\" + filename)  # Adding the pdf complete location in the list.
                self.image_list.append("E:\Wallpapers\\" + filename)  # Adding the mp4 file name addition ,
        self.image_list.sort(key=str.lower)
        return self.image_list  # This returns the image list in the for of sorted format!

        # Getting the current image list

    def current_image(self):
        if len(self.image_list) > 1:
            print(self.image_list[self.position])  # This prints out the specific music
        else:
            print("No images found! ")  # There is no music found

    # Getting the next image in the particular directory from the list
    def next_image(self):
        if self.position + 1 < len(self.image_list):
            # Checking if the position of the Specific is less than the other one
            self.position += 1
            # print(self.image_list[self.position])
            #  Prints out the current list of the image viewer
            return self.image_list[self.position]
            # Returned the image from the specified music list and the position of the list
        else:
            return self.image_list[self.position]  # returns the music value

    # Getting the previous image in the items of the list ...
    def previous_image(self):
        if self.position - 1 >= 0 and len(self.image_list) > 1:  # Two condition checking for the specified list
            self.position -= 1
            # print(self.music_list[self.position])
            return self.image_list[self.position]  # Returns to the called function
        else:  # The else condition is kept running !
            return self.image_list[self.position]  # Returns the default music element to the called funciton
            # sorting the Music player

    # Viewing tehe images
    def view_image_file(self, locationfile):
        try:
            print("start  " + locationfile)
            os.system("start  " + locationfile)  # This will start the particular music
        except Exception as Ex:
            print("check the directory exception", Ex)

    def display_image(self):
        self.view_image_file(self.image_list[self.position])
# The main function is just for the testing purpose .. !!!!
# def main():
#     print("Testing ")
#     ic = IMAGE_CHECK()  # creating the image check object !
#     ic.display_image()
#     time.sleep(5)
#     ic.view_image_file(ic.next_image())

# main()

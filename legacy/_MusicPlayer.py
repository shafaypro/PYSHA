import pygame
class MusicPlayer:
    def __init__ (self):
        pygame.mixer.init()
        # this class will be responsible for the playing of the music and the specific things

    def play_music (self, song_name=""):
        pygame.mixer.music.load(song_name)  # this loads the Pygame music in the pygame module
        pygame.mixer.music.play()  # plays the music specified.
        pass  # here you will be adding the features for playing the music

    def stop_music (self):
        pygame.mixer.music.stop()  # Stops the Music Which is being played

    def play_music_start (self,
                          song_name):  # here the play music will be provided with the starting and the ending of the music.
        pass

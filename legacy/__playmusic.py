import pyglet
from pyglet.gl import *
song  = pyglet.media.load("Music\\WithoutEnd.mp3")  # this file name is the specified directory
song.play() # this is the playing for the song
pyglet.app.run() # this runs the Pyglet application


#
# import pyglet
# pyglet.lib.load_library('avbin')
# pyglet.have_avbin=True
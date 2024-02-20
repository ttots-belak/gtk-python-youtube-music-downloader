import gi
from os import mkdir, system
from pytube import YouTube 
from pytube.exceptions import VideoUnavailable
from pytube import Playlist 
import ffmpeg
from mutagen.mp3 import MP3  
from mutagen.easyid3 import EasyID3
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
def check_and_download(window, args):
    user_input_needed = ""
    user_input_correct = True
    if "link" not in args:
        user_input_correct = False
        user_input_needed = user_input_needed + "link "
    if "folder" not in args:
        user_input_correct = False
        user_input_needed = user_input_needed + "folder "
    if not user_input_correct:
        dialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.ERROR,
            Gtk.ButtonsType.OK, "ARR NARRR")
        dialog.format_secondary_text(
                "You are missing the following things: " + user_input_needed)
        dialog.run()
        dialog.destroy()
        return 
    try:
        artist = args["artist"]
    except:
        artist = ""
    try:
        album = args["album"]
    except:
        album = ""

    if args["is_album"] == True:
        play = Playlist(args["link"]) 
        play_folder = args["folder"] + "/" + play.title
        mkdir(play_folder)
        print(play_folder)
        for link in play.video_urls:
            dl_audio(window, link, args["ft"], play_folder, artist, album)
    elif args["is_album"] == False:
        dl_audio(window, args["link"], args["ft"], args["folder"], artist, album)

def error_message(window, message):
    
    dialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.ERROR,
        Gtk.ButtonsType.OK, "ARR NARRR")
    dialog.format_secondary_text(
            message)
    dialog.run()
    dialog.destroy()

def dl_message(window, message):
    
    dialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.INFO,
                               Gtk.ButtonsType.OK, "YO!")
    dialog.format_secondary_text(
            message)
    dialog.run()
    dialog.destroy()
def dl_audio(window, link, file_type, folder, artist, album):
        try:
            vid = YouTube(link)
        except:
            error_message(window, "The video doesn't exist or is unavailable")
            return
        stream = vid.streams.filter(only_audio=True, adaptive=True).get_audio_only()
        path_to_vid = stream.download(output_path=folder)
        path_to_audio = path_to_vid[:-4] + file_type
        ffmpeg.input(path_to_vid).output(path_to_audio).run()
        if file_type == ".mp3":
            system("eyeD3 -a '" + artist + "' -A '" + album + "' '" + path_to_audio + "'")
        system("rm '" + path_to_vid + "'")

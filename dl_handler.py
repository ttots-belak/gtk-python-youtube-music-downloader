import gi
from os import mkdir, system
from pytube import YouTube 
from pytube import Playlist 
import ffmpeg
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
def check_and_download(window, link, folder, filetype, add_trackno):
    if link is None or folder is None or filetype is None:
        error_message(window, "Required fields are missing!!!!!")
        return
    if "playlist" in link:
        play = Playlist(link) 
        play_folder = folder + "/" + play.title
        trackno = 1
        for vid in play.video_urls:
            dl_audio(window, vid, filetype, play_folder, play.title, trackno, play.length, add_trackno)
            trackno = trackno + 1
    elif "watch" in link:
        dl_audio(window, link, filetype, folder, append_track_no=add_trackno)
    else:
        error_message(window, "Couldn't parse link!")

def error_message(window, message):
    
    dialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.ERROR,
        Gtk.ButtonsType.OK, "ARR NARRR")
    dialog.format_secondary_text(
            message)
    dialog.run()
    dialog.destroy()

def info_message(window, message):
    
    dialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.INFO,
                               Gtk.ButtonsType.OK, "YO!")
    dialog.format_secondary_text(
            message)
    dialog.run()
    dialog.destroy()
def dl_audio(window, link, file_type, folder, album = "", track_no = 0, track_total = 0, append_track_no = False):
        try:
            vid = YouTube(link)
        except:
            error_message(window, "The video doesn't exist or is unavailable")
            return
        stream = vid.streams.filter(only_audio=True, adaptive=True).get_audio_only()
        path_to_vid = stream.download(output_path=folder)
        title = path_to_vid[len(folder) + 1:-4]
        if append_track_no == True:
            path_to_audio = f'{path_to_vid[:-(len(title) + 4)]}{track_no:02}_{title}{file_type}'
        else:
            path_to_audio = path_to_vid[:-4] + file_type
        ffmpeg.input(path_to_vid).output(path_to_audio).run()
        if file_type == ".mp3":
                system('eyeD3 -a "' + vid.author.replace(" - Topic", "") + 
                       '" -A "' + album.replace("Album - ", "") + 
                       '" -t "' + vid.title + 
                       '" -n ' + str(track_no) + 
                       ' -N ' + str(track_total) + 
                       ' "' + path_to_audio + '"')
        system('rm "' + path_to_vid + '"')
        



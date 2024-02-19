import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
args = {
        "ft": ".mp3"
        } #Should have "link", "folder", "ft" (filetype) and "is_album". can also have "artist" and "album"
builder = Gtk.Builder()
builder.add_from_file("wow.glade")

class Handlers:
    """called when the x button is pressed"""
    def main_window_destroy_cb(self, _):
        Gtk.main_quit()

    """called when enter is pressed in the link input box"""
    def link_activate_cb(self, link):
        args["link"] = link.get_text()

    """called when a folder is set in the dialogue"""
    def dir_choice_file_set_cb(self, file):
        args["folder"] = file.get_filename()

    def album_choice_toggled_cb(self, button):
        args["is_album"] = button.get_active()

    def artist_choice_activate_cb(self, artist):
        args["artist"] = artist.get_text()

    def album_choice_activate_cb(self, album):
        args["album"] = album.get_text()

    def filetype_choice_changed_cb(self, choice):
        choice_id = choice.get_active_id()
        args["ft"] = ".mp3" if choice_id == "0" else ".wav"
    """called when the download button is pressed"""
    def download_clicked_cb(self, _):
        #TODO: create function in dl_handler.py to handle downloading all of the files
        print("args:" + str(args))

    """called when the cancel button is pressed"""
    def cancel_clicked_cb(self, _):
        Gtk.main_quit()

builder.connect_signals(Handlers())
window = builder.get_object("main_window")
window.show_all()
Gtk.main()

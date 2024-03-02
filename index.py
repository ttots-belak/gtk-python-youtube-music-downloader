import gi

from dl_handler import check_and_download
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
builder = Gtk.Builder()
builder.add_from_file("wow.glade")

class Handlers:
    filetype = None
    add_trackno = False
    link = None
    folder = None
    """called when the x button is pressed"""
    def main_window_destroy_cb(self, _):
        Gtk.main_quit()

    """called when enter is pressed in the link input box"""
    def link_activate_cb(self, text):
        self.link = text.get_text()


    def link_paste_cb(self, text):
        self.link = text.get_text()
    """called when a folder is set in the dialogue"""
    def dir_choice_file_set_cb(self, file):
        self.folder = file.get_filename()

    def filetype_choice_changed_cb(self, choice):
        choice_id = choice.get_active_id()
        self.filetype = ".mp3" if choice_id == "0" else ".wav"
    
    def add_trackno_toggled_cb(self, tick):
        self.add_trackno = not self.add_trackno 
    """called when the download button is pressed"""
    def download_clicked_cb(self, _):
        print(f"link: {self.link}\nfolder: {self.folder}\nfiletype: {self.filetype}\nadd_trackno: {self.add_trackno}")
        download_jump(self.link, self.folder, self.filetype, self.add_trackno)

    """called when the cancel button is pressed"""
    def cancel_clicked_cb(self, _):
        Gtk.main_quit()

builder.connect_signals(Handlers())
window = builder.get_object("main_window")
window.show_all()
def download_jump(link, folder, filetype, add_trackno):
    check_and_download(window, link, folder, filetype, add_trackno)
Gtk.main()

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyApp:
    def __init__(self):

        # Load the Glade file to construct the GUI
        self.builder = Gtk.Builder()
        self.builder.add_from_file("wow.glade")

        # Retrieve the main window from Glade and set up the close event
        self.window = self.builder.get_object("window1")
        self.window.connect("destroy", Gtk.main_quit)







    def run(self):
        self.window.show_all()
        Gtk.main()

if __name__ == "__main__":
    app = MyApp()
    app.run()

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class AppWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="PenPal")
        self.set_border_width(10)
        self.set_default_size(500, 450)

        header = Gtk.HeaderBar(title="PenPal")
        header.set_subtitle("A Simple Cipher app")
        header.props.show_close_button = True

        self.set_titlebar(header)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        flowbox = Gtk.FlowBox()
        flowbox.set_valign(Gtk.Align.START)
        flowbox.set_max_children_per_line(30)
        flowbox.set_selection_mode(Gtk.SelectionMode.NONE)

        self.message = Gtk.TextView()
        self.set_default_size(-1, 350)
        self.textbuffer = self.message.get_buffer()
        self.textbuffer.set_text("Welcome to the PenPal Cipther App!")
        self.message.set_editable(True)

        label = Gtk.Label()
        label.set_text("Enter the message that you want to encode/decode.")

        button = Gtk.Button.new_with_label("Encode/Decode")
        button.connect("clicked", self.on_encode_clicked)
                
        flowbox.add(label)
        flowbox.add(self.message)
        flowbox.add(button)

        scrolled.add(flowbox)

        self.add(scrolled)
        self.show_all()

    def on_encode_clicked(self, button):
        print("Encode button clicked. This is where we put the code April wrote")

win = AppWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
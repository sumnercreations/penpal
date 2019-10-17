import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from decoder import decode
from encoder import encode

class AppWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="PenPal")
        self.set_border_width(10)
        self.set_default_size(500, 450)

        header = Gtk.HeaderBar(title="PenPal")
        header.set_subtitle("A Simple Cipher app")
        header.props.show_close_button = True

        self.set_titlebar(header)

        # TODO: layout would paned or stack work better than flowbox?
        flowbox = Gtk.FlowBox()
        flowbox.set_valign(Gtk.Align.START)
        flowbox.set_max_children_per_line(30)
        flowbox.set_selection_mode(Gtk.SelectionMode.NONE)

        # TODO: add input for the shift
        # Gtk.Scale or Gtk.SpinButton?

        # start decoder
        self.message_to_decode = Gtk.TextView()
        self.message_to_decode.set_size_request(300,50)
        self.textbuffer = self.message_to_decode.get_buffer()
        self.textbuffer.set_text("awecvgy Dlsjvtl av aol WluWhs Jpwoly Hww!")
        self.message_to_decode.set_editable(True)

        decode_label = Gtk.Label()
        decode_label.set_text("Enter the message that you want to decode.")

        decode_button = Gtk.Button.new_with_label("Decode Message")
        decode_button.connect("clicked", self.on_decode_clicked)

        self.decoded_label = Gtk.Label()
        self.decoded_label.set_selectable(True)
        # /end decoder

        # TODO: try using the Frame or Paned to separate the 2
        # separator
        separator = Gtk.Separator()

        # start encoder
        self.message_to_encode = Gtk.TextView()
        self.message_to_encode.set_size_request(300,50)
        self.textbuffer = self.message_to_encode.get_buffer()
        self.textbuffer.set_text("Welcome to the PenPal Cipher App!")
        self.message_to_encode.set_editable(True)

        encode_label = Gtk.Label()
        encode_label.set_text("Enter the message that you want to encode.")

        encode_button = Gtk.Button.new_with_label("Encode Message")
        encode_button.connect("clicked", self.on_encode_clicked)

        self.encoded_label = Gtk.Label()
        self.encoded_label.set_selectable(True)
        # /end encoder

        flowbox.add(decode_label)
        flowbox.add(self.message_to_decode)
        flowbox.add(decode_button)
        flowbox.add(self.decoded_label)
        flowbox.add(separator)
        flowbox.add(encode_label)
        flowbox.add(self.message_to_encode)
        flowbox.add(encode_button)
        flowbox.add(self.encoded_label)

        self.add(flowbox)
        self.show_all()

    def on_decode_clicked(self, button):
        buffer = self.message_to_decode.get_buffer()
        (start, stop) = buffer.get_bounds()
        message_to_decode = buffer.get_text(start, stop, 0)
        decoded_message = decode(message_to_decode)

        # display the decoded message
        self.decoded_label.set_text(decoded_message)
    
    def on_encode_clicked(self, button):
        buffer = self.message_to_encode.get_buffer()
        (start, stop) = buffer.get_bounds()
        message_to_encode = buffer.get_text(start, stop, 0)
        encoded_message = encode(message_to_encode, 7)

        # display the encoded message
        self.encoded_label.set_text(encoded_message)

win = AppWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
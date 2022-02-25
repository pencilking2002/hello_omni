import omni.ext
import omni.ui as ui

""" 
Simple Code Omniverse extension that displays a label
and an input field that is connected to the label. 
If there's nothing in the field, a default message is displayed
"""


class MyExtension(omni.ext.IExt):
    def __init__(self):
        self.title_style = {
            "alignment": ui.Alignment.CENTER_TOP,
            "height": 50,
            "color": "0xFFF0000",
            "font_size": 20,
            "background_color": "0xFF00DDDD",
        }

        self.field_style = {"background_color": "white", "color": "black", "border_color": "black", "border_width": 1}
        self.title = "HELLO OMNI"

    def on_startup(self, ext_id):

        self._window = ui.Window(self.title, width=300, height=150)

        with self._window.frame:
            with ui.VStack():
                label = ui.Label(self.title, style=self.title_style)

                ui.Label("Start typing here to change the title", alignment=ui.Alignment.CENTER_TOP, height=30)

                field = ui.StringField(style=self.field_style)
                field.model.set_value(self.title)
                field.model.add_value_changed_fn(lambda model, label=label: self.setText(label, model))

    # Callback method for text changes in the input field
    def setText(self, label, model):
        value = model.get_value_as_string().strip()
        if len(value) == 0:
            label.text = "NO TITLE"
        else:
            label.text = value

    def on_shutdown(self):
        print("[omni.hello.world] MyExtension shutdown")

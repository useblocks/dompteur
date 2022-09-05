
from dompteur.ui import DompteurApp


class SimpleStart(DompteurApp):
    def open_create(self):
        self.create_window = self.builder.get_object("create", None)
        self.create_window.mainloop()


    def raise_frame(self, *args):
        pass

if __name__ == "__main__":
    app = SimpleStart()
    app.run()

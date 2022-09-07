#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class DompteurWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(DompteurWidget, self).__init__(master, **kw)
        self.panedwindow3 = ttk.Panedwindow(self, orient="horizontal")
        self.SphinxFrame = ttk.Frame(self.panedwindow3)
        self.SphinxFrame.configure(borderwidth=0, style="Sphinx_M.TFrame", width=300)
        self.label5 = ttk.Label(self.SphinxFrame)
        self.img_sphinx_blue_small_logo = tk.PhotoImage(
            file="sphinx_blue_small_logo.png"
        )
        self.label5.configure(
            background="#0a507a",
            font="TkDefaultFont",
            image=self.img_sphinx_blue_small_logo,
            justify="center",
            style="Sphinx.TLabel",
            text="label5",
        )
        self.label5.pack(pady=0, side="top")
        self.label3 = ttk.Label(self.SphinxFrame)
        self.label3.configure(
            padding="20 0", style="Sphinx_M.TLabel", text="Sphinx SimpleStart"
        )
        self.label3.pack(side="top")
        self.label20 = ttk.Label(self.SphinxFrame)
        self.label20.configure(
            padding="20 0",
            style="Sphinx_M_small.TLabel",
            takefocus=False,
            text="👁 Project Overview",
        )
        self.label20.pack(pady="0 40", side="top")
        self.button18 = ttk.Button(self.SphinxFrame)
        self.button18.configure(
            compound="top",
            default="disabled",
            style="Sphinx_M.TButton",
            takefocus=True,
            text="🖴 Import Project",
        )
        self.button18.pack(
            anchor="n", expand="false", fill="x", padx=15, pady=5, side="top"
        )
        self.button17 = ttk.Button(self.SphinxFrame)
        self.button17.configure(
            compound="top",
            cursor="arrow",
            default="disabled",
            state="normal",
            style="Sphinx_M.TButton",
            takefocus=True,
            text="📦 Create Project",
        )
        self.button17.pack(
            anchor="n", expand="false", fill="x", padx=15, pady=5, side="top"
        )
        self.button17.configure(command=self.open_create)
        self.frame1 = ttk.Frame(self.SphinxFrame)
        self.frame1.configure(
            height=30, style="Sphinx_M.TFrame", takefocus=False, width=200
        )
        self.frame1.pack(side="top")
        self.SphinxFrame.pack(side="top")
        self.panedwindow3.add(self.SphinxFrame, weight="0")
        self.frame5 = ttk.Frame(self.panedwindow3)
        self.frame5.configure(
            cursor="arrow",
            height=100,
            style="Sphinx_R.TFrame",
            takefocus=False,
            width=200,
        )
        self.frame6 = ttk.Frame(self.frame5)
        self.frame6.configure(height=2, style="Sphinx_R.TFrame", width=200)
        self.label1 = ttk.Label(self.frame6)
        self.label1.configure(
            anchor="n",
            justify="right",
            style="Sphinx_R.TLabel",
            text="Project X",
            width=20,
        )
        self.label1.grid(column=0, ipadx=0, row=0)
        self.button8 = ttk.Button(self.frame6)
        self.button8.configure(style="Sphinx_R.TButton", text="Build")
        self.button8.grid(column=1, padx=2, row=0)
        self.combobox2 = ttk.Combobox(self.frame6)
        self.combobox2.configure(
            exportselection="true", validate="focusin", values="HTML PDF JSON", width=10
        )
        self.combobox2.grid(column=2, padx=0, row=0)
        self.button_show = ttk.Button(self.frame6)
        self.button_show.configure(
            cursor="arrow", style="Sphinx_R.TButton", text="Show"
        )
        self.button_show.grid(column=4, padx=2, row=0)
        self.conf = ttk.Button(self.frame6)
        self.conf.configure(style="Sphinx_R.TButton", text="Configure")
        self.conf.grid(column=65, padx=20, row=0)
        self.frame6.pack(pady=20, side="top")
        self.frame6.grid_anchor("center")
        self.frame8 = ttk.Frame(self.frame5)
        self.frame8.configure(height=2, style="Sphinx_R.TFrame", width=200)
        self.label2 = ttk.Label(self.frame8)
        self.label2.configure(
            anchor="n",
            style="Sphinx_R.TLabel",
            takefocus=True,
            text="Project Y",
            width=20,
        )
        self.label2.grid(column=0, ipadx=0, row=0)
        self.button14 = ttk.Button(self.frame8)
        self.button14.configure(style="Sphinx_R.TButton", text="Build")
        self.button14.grid(column=1, padx=2, row=0)
        self.combobox4 = ttk.Combobox(self.frame8)
        self.combobox4.configure(
            justify="left", validate="focusout", values="HTML PDF", width=10
        )
        self.combobox4.grid(column=2, row=0)
        self.button15 = ttk.Button(self.frame8)
        self.button15.configure(cursor="arrow", style="Sphinx_R.TButton", text="Show")
        self.button15.grid(column=4, padx=2, row=0)
        self.button16 = ttk.Button(self.frame8)
        self.button16.configure(style="Sphinx_R.TButton", text="Configure")
        self.button16.grid(column=65, padx=20, row=0)
        self.frame8.pack(side="top")
        self.frame8.grid_anchor("center")
        self.frame5.pack(side="top")
        self.panedwindow3.add(self.frame5)
        self.panedwindow3.pack(expand="true", fill="both", side="top")
        self.configure(
            background="#41799c",
            cursor="arrow",
            height=200,
            relief="flat",
            takefocus=False,
        )
        self.title("Dompteur")

        self.setup_ttk_styles()

    def setup_ttk_styles(self):
        # ttk styles configuration
        self.style = style = ttk.Style()
        optiondb = style.master
        # --------------------
        # This file is used for defining Ttk styles.
        # Use the 'style' object to define styles.

        # Pygubu Designer will need to know which style definition file
        # you wish to use in your project.

        # To specify a style definition file in Pygubu Designer:
        # Go to: Edit -> Preferences -> Ttk Styles -> Browse (button)

        # In Pygubu Designer:
        # Assuming that you have specified a style definition file,
        # - Use the 'style' combobox drop-down menu in Pygubu Designer
        #   to select a style that you have defined.
        # - Changes made to the chosen style definition file will be
        #   automatically reflected in Pygubu Designer.
        # --------------------

        # Example code:

        # Left menu config
        style.configure("Sphinx_M.TFrame", background="#0A507A")
        style.configure(
            "Sphinx_M.TLabel",
            background="#0A507A",
            font=("helvetica", 12, "bold"),
            foreground="#ffffff",
        )
        style.configure(
            "Sphinx_M_small.TLabel",
            background="#0A507A",
            font=("helvetica", 10),
            foreground="#ffffff",
        )

        style.configure(
            "Sphinx_M.TButton",
            relief="flat",
            background="#FFFFFF",
            font=("helvetica", 12),
        )

        #
        # Right area config
        #
        style.configure("Sphinx_R.TFrame", background="#eeeeee")

        # TLabel
        style.configure(
            "Sphinx_R.TLabel",
            background="#eeeeee",
            font=("helvetica", 12, "bold"),
            foreground="#000000",
        )
        style.configure(
            "Sphinx_R_small.TLabel",
            background="#eeeeee",
            font=("helvetica", 10),
            foreground="#000000",
        )
        style.configure(
            "Sphinx_R_title.TLabel",
            background="#eeeeee",
            font=("helvetica", 14, "bold"),
            foreground="#000000",
        )

        # Entry
        style.configure(
            "Sphinx_R.TEntry",
            background="#eeeeee",
            font=("helvetica", 12, "bold"),
            foreground="#000000",
        )

        style.configure(
            "Sphinx_R.TButton",
            relief="flat",
            # relief="raised",
            background="#777777",
            foreground="#FFFFFF",
            font=("helvetica", 10),
            activebackground="#555555",
            activeforground="#FF0055",
            highlightbackground="#222222",
            highlightforeground="#FF0055",
        )

        style.map(
            "Sphinx_R.TButton",
            foreground=[("pressed", "#FFFFFF"), ("active", "#FFFFFF")],
            background=[("pressed", "!disabled", "#555555"), ("active", "#444444")],
        )

    def open_create(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = DompteurWidget(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

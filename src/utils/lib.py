import tkinter as tk

def add_placeholder(entry:tk.Entry, placeholder_text:str):
        def on_focus_in(event):
            if entry.get() == placeholder_text:
                entry.delete(0, tk.END)
                entry.config(fg='black')  # restore normal text color

        def on_focus_out(event):
            if entry.get() == '':
                entry.insert(0, placeholder_text)
                entry.config(fg='gray')   # placeholder color

        entry.insert(0, placeholder_text)
        entry.config(fg='gray')
        entry.bind('<FocusIn>', on_focus_in)
        entry.bind('<FocusOut>', on_focus_out)
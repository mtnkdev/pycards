"""This module is responsible for the creation of the progress bar
when the application is being loaded

    State Variables:
    root: the application window

    Environment Variables:
    system display: array of pixels used for graphical output


"""
import sys
if sys.version_info[0] < 3:
    import Tkinter
    import ttk
else:
    import tkinter as Tkinter
    import tkinter.ttk as ttk
import time
    


def create(root, delay):
    """Create progressbar"""
    root.wm_withdraw()
    style = ttk.Style()
    style.theme_use("alt")
    style.configure("green.Horizontal.TProgressbar", foreground="#08C715", background="#08C715", orient='horizontal')

    loader = Tkinter.Toplevel(background="#5c5a58")
    loader.geometry("400x100")
    loader.wm_title('Loading PyCards')
    loader.bar = ttk.Progressbar(loader, style="green.Horizontal.TProgressbar", mode="determinate", length=300)
    loader.bar['value'] = 0
    loader.bar['maximum'] = 400
    loader.bar.pack(anchor=Tkinter.CENTER, expand=True)
    loader.resizable(0,0)

    def action():
        """Increments progress on the bar"""
        for step in range(0, int(loader.bar['maximum']), int(loader.bar['maximum'] / 10)):
            loader.bar['value'] = step
            time.sleep(delay)
            loader.update()
        loader.wm_withdraw()
        loader.destroy()
    action()

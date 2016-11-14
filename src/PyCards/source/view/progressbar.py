import Tkinter
import time
import ttk


def create(root, delay):
    """Creates progressbar"""
    root.wm_withdraw()
    style = ttk.Style()
    style.theme_use("alt")#PySolFC uses classic
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
        for step in range(0, int(loader.bar['maximum']), loader.bar['maximum'] / 10):
            loader.bar['value'] = step
            time.sleep(delay)
            loader.update()
        loader.wm_withdraw()
        loader.destroy()
    action()

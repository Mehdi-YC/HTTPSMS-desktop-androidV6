try:
    import tkinter as tk
except ModuleNotFoundError:
    import Tkinter as tk  # Python 2.
import time
import winsound



class Application(tk.Frame, object):
    def __init__(self, master=None):
        super(Application, self).__init__(master)  # Call baseclass constructor.
        self.after_id = None
        self.secs = 0
        self.c = 0
        # Create widgets,
        startButton = tk.Button(top, height=2, width=20, text="Start", command=self.start)
        stopButton = tk.Button(top, height=2, width=20, text="Stop", command=self.stop)
        startButton.pack()
        stopButton.pack()

    def beeper(self):
        self.secs += 1
        if self.secs % 2 == 0:  # Every other second.
            #winsound.Beep(FREQ, DUR)
            print("counter : ",self.c)
            self.c+=1
        self.after_id = top.after(500, self.beeper)  # Check again in 1 second.

    def start(self):
        self.secs = 0
        self.beeper()  # Start repeated checking.

    def stop(self):
        if self.after_id:
            top.after_cancel(self.after_id)
            self.after_id = None


if __name__ == '__main__':

    top = tk.Tk()
    app = Application()
    app.master.title('MapAwareness')
    app.master.geometry('200x100')
    app.mainloop()
    
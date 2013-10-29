import tkinter
from time import strftime


class Relogio(tkinter.Label):

    def __init__(self):
        tkinter.Label.__init__(self)
        self.pack()
        self['text'] = strftime('%H:%M:%S')
        self['font'] = 'Helvetica 120 bold'
        self.tictac()

    def tictac(self):
        agora = strftime('%H:%M:%S')
        if agora != self['text']:
            self['text'] = agora
        self.after(100, self.tictac)

rel = Relogio()
rel.mainloop()

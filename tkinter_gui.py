from tkinter import *

class StartMenu:

    def __init__(self, master, on_go_function, on_go_args):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.on_go_function = on_go_function
        self.on_go_args = on_go_args
        self.run_processes = Button(frame, text="Run Program", command=self.run_it)
        self.run_processes.pack(side=LEFT)
       
    def run_it(self):
        self.on_go_function(self.on_go_args)


# root = Tk()

# def sample_fxn(sample_args):
#     print('arg1:', sample_args['arg1'])
#     print('arg2:', sample_args['arg2'])
#     print('arg3:', sample_args['arg3'])

# sample_args = {'arg1': 1, 'arg2': 2, 'arg3': 3}

# menu = StartMenu(root, sample_fxn, sample_args)
# root.mainloop()
# root.destroy() # optional; see description below
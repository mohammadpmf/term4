from myclass import *

root = Tk()
game = AddMyGame(root, text="Game Info", labelanchor='n', padx=5, pady=5, bg='sky blue', fg='red', fg2='green', font=('Times', 20), relief='raised')
game.grid()
root.mainloop()
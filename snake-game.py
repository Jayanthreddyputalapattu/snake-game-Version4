from tkinter import *



window = Tk()
window.title("snake-game-version4")
window.geometry("500x500")


head = PhotoImage("square.png")
Label(window,image=head,bg="black") .grid(row=0,column=0,sticky=E)








window.mainloop()
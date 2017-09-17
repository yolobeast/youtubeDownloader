import tkinter as tk
from tkinter import messagebox
from youtube import download
from converter import converter

def About():
   toplevel = tk.Toplevel()
   toplevel.geometry("600x250")
   toplevel.resizable(False, False)
   toplevel.title('About')
   toplevel.focus_set()
   t = tk.Text(toplevel, height = 600, width = 250)
   t.pack()
   quote = """HAMLET: To be, or not to be--that is the question:
            Whether 'tis nobler in the mind to suffer
            The slings and arrows of outrageous fortune
            Or to take arms against a sea of troubles
            And by opposing end them. To die, to sleep--
            No more--and by a sleep to say we end
            The heartache, and the thousand natural shocks
            That flesh is heir to. 'Tis a consummation
            Devoutly to be wished."""
   t.insert(tk.END, quote)
   t.config(state=tk.DISABLED)
   
def action():
    inputvalue = t.get("1.0",'end-1c')
    ret = download(inputvalue)
    if (ret == 0) :
        messagebox.showinfo("Error", "The link you have entered is not a video")
    print (inputvalue)
    
def convertAction():
    converter()
    
root = tk.Tk()
root.geometry("525x250")
root.resizable(False, False)
menu = tk.Menu(root)
root.config(menu=menu)
aboutmenu = tk.Menu(menu)
menu.add_cascade(label="About", menu=aboutmenu)
aboutmenu.add_command(label="About", command=About)

labelOne=tk.Label(root, text = "Enter a video link below :")
labelOne.place(x=5,y=25)

t = tk.Text(root, height = 3, width = 50)
t.place(x = 5,y = 50)
quote = """Please enter a video link"""
t.insert(tk.END,"")

button = tk.Button(root, height=3,width=12,text='Download video', command=action)
button.place(x = 415,y = 49)


labelOne=tk.Label(root, text = "Enter a video link below :")
labelOne.place(x=5,y=150)
buttonTwo = tk.Button(root, height=3,width=12,text='Convert to Mp3', command=convertAction)
buttonTwo.place(x = 120,y = 175)

root.mainloop()
    




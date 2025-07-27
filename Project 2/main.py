import tkinter as tik

root = tik.Tk()
root.title("Login")
width = 900
height = 600
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
x = (screenwidth // 2) - (width // 2)
y = (screenheight // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")
root.config(bg="#f9b34f")
root.resizable(False,False)
root.mainloop()

# ---------------------------- Imports!!!! --------------------------
import tkinter as tk
from tkinter import messagebox
import sys 
import pygame
import json
import game

# --------------- Setting Tkinterrrrrr!!!!!! ------------------------------------------
root = tk.Tk()
root.title("MainScreen")
root.geometry("1200x600")
root.resizable(False,False)

def load_settings():
    file_path = "settings.json"
    try:
        with open(file_path, 'r') as f:
            settings_dict = json.load(f)
        print(f"Settings loaded from {file_path}")
        return settings_dict
    except FileNotFoundError:
        print(f"Settings file '{file_path}' not found. Using default settings.")
        return {
            "music_volume": 0.75
        }
    except json.JSONDecodeError as e:
        print(f"Error decoding settings file: {e}. Using default settings.")
        return {
            "music_volume": 0.75
        }

# ------------------Int,Bool,Float,String -------------------------------
padymaintitle = int(50)
currentpadytitle = padymaintitle
animationstart = False
loaded_settings = load_settings()
musicvol = tk.DoubleVar()
musicvol.set(loaded_settings.get("music_volume", 0.75))


# ------------ Functionsssssssssssss!!!!!!! ------------------------------ 
def start_game():
    print("The game has ben start")
    root.destroy()
    game.run_game()

def settings_game():
    print("User open settings window!")
    if animationstart == False:
        animationmaintosettings()
    else:
        MainTitle.pack_forget()
        ButtonPlay.pack_forget()
        ButtonSettings.pack_forget()
        ButtonQuit.pack_forget()
        TitleScreenSettings.place(x=490,y=50)
        Buttonsave.place(x=1000,y=520)
        Buttonback.place(x=800,y=520)
        AudioLable.place(x=20,y=120)
        AudioScale.place(x=20,y=180)

def update_music_volume(val):
    volume = float(val)
    print(f"Music volume is now: {volume * 100:.0f}%")

# ------------------- make animation all tinkers pull down with animation
def animationmaintosettings():
    global currentpadytitle
    global animationstart
    
    targetpadytitle = 400
    if currentpadytitle < targetpadytitle:
        currentpadytitle += 5
        MainTitle.pack_forget()
        MainTitle.pack(padx=600/2,pady=currentpadytitle)
        ButtonPlay.pack_forget()
        ButtonPlay.pack(padx=600/2,pady=currentpadytitle)
        ButtonSettings.pack_forget()
        ButtonSettings.pack(padx=600/2,pady=currentpadytitle)
        ButtonQuit.pack_forget()
        ButtonQuit.pack(padx=600/2,pady=currentpadytitle)
        root.after(10, animationmaintosettings)
    else:
        print("Function end!")
        animationstart = True
        MainTitle.pack_forget()
        ButtonPlay.pack_forget()
        ButtonSettings.pack_forget()
        ButtonQuit.pack_forget()
        TitleScreenSettings.place(x=490,y=50)
        Buttonsave.place(x=1000,y=520)
        Buttonback.place(x=800,y=520)
        AudioLable.place(x=20,y=120)
        AudioScale.place(x=20,y=180)


# ---------------- save settings in json file!!! -----------------------------
def savesettings():
    print("The user Apply the Settings!")
    current_settings = {
        "music_volume": musicvol.get()
    }
    
    _save_settings_to_file(current_settings)


def _save_settings_to_file(settings_dict):
    file_path = "settings.json"
    try:
        with open(file_path, 'w') as f:
            json.dump(settings_dict, f, indent=4)
        print(f"Settings saved to {file_path}")
    except IOError as e:
        print(f"Error saving settings: {e}")


def backsettings():
    global currentpadytitle
    global animationstart
    print("The user Back the Settings!")
    TitleScreenSettings.place_forget()
    Buttonsave.place_forget()
    Buttonback.place_forget()
    AudioLable.place_forget()
    AudioScale.place_forget()
    currentpadytitle = padymaintitle
    animationstart = False
    MainTitle.pack(padx=600/2,pady=50)
    ButtonPlay.pack(padx=600/2,pady=20)
    ButtonSettings.pack(padx=600/2,pady=20)
    ButtonQuit.pack(padx=600/2,pady=20)


def exit_game():
    if messagebox.askyesno("Exit", "Do you sure want to quit from the game?"):
        sys.exit()


#                         Add tk to mainscreen
# -------------------- Adding Title not a screen title!!! ----------------------------------
MainTitle = tk.Label(root,text="ChronoEcho: The Temporal Labyrinth", font=("Arial",24,"bold"),fg="darkblue")
MainTitle.pack(padx=600/2,pady=50)

# ---------------------- Adding Button START PLAY!!!!!!!!! ---------------------------------------
ButtonPlay = tk.Button(root,text="StartPlay", font=("Arial",16),command=start_game,bg="lightgreen",fg="Black",width=15,height=2)
ButtonPlay.pack(padx=600/2,pady=20)

# ---------------------- Adding Button Settings!!!!!!!!! ---------------------------------------
ButtonSettings = tk.Button(root,text="Settings", font=("Arial",16),command=settings_game,bg="White",fg="Black",width=15,height=2)
ButtonSettings.pack(padx=600/2,pady=20)

# ---------------------- Adding Button Close!!!!!!!!! ---------------------------------------
ButtonQuit = tk.Button(root,text="Quit", font=("Arial",16),command=exit_game,bg="Red",fg="Black",width=15,height=2)
ButtonQuit.pack(padx=600/2,pady=20)

#                         Add tk to settingsscreen
# ------------------ Adding Title Lable -----------------------------
TitleScreenSettings = tk.Label(root,text="Settings",font=("Arial",40,"bold"),fg="darkblue")
TitleScreenSettings.place(x=0,y=600000)

# ------------------ Adding Button Apply Settings -----------------------------
Buttonsave = tk.Button(root,text="Apply Settings",font=("Arial", 16), command=savesettings,bg="Yellow",fg="black",width=15,height=2)
Buttonsave.place(x=0,y=1000000)

# ----------------- Adding Button Back Settings -------------------------------
Buttonback = tk.Button(root,text="Back Settings",font=("Arial", 16), command=backsettings,bg="Red",fg="black",width=15,height=2)
Buttonback.place(x=0,y=1000000)

# ----------------- Adding Audio Text Lable -------------------------------
AudioLable = tk.Label(root,text="#Audio#",font=("Arial",24,"bold"),fg="black")
AudioLable.place(x=0,y=1000000)

# ----------------- Adding Scale Audio Setting -------------------------------
AudioScale = tk.Scale(root,from_=0,to=1.0,orient=tk.HORIZONTAL,resolution=0.01,label="Music Volume", font=("Arial",12),length=300,variable=musicvol,command=update_music_volume,showvalue=True)
AudioScale.place(x=0,y=1000000)


# ------------------- Start The Window!!!! ---------------------------------
root.mainloop()

print("Game In Progress!")
import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

root.title('Workspace Opener')

apps = []

if os.path.isfile('save.txt'):
	with open('save.txt', 'r') as f:
		tempApps = f.read()
		tempApps = tempApps.split(',')
		apps = [x for x in tempApps if x.strip()]

def addApp():
	for widget in frame.winfo_children():
		widget.destroy()

	filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
	apps.append(filename)
	print(filename)
	for app in apps:
		label = tk.Label(frame, text=app, bg="gray")
		label.pack()

def runApps():
	for app in apps:
		os.startfile(app)

canvas = tk.Canvas(root, height=500, width=700, bg="#263d42")
canvas.pack()

frame = tk.Frame(root, bg="#f4f4f4")
frame.place(relwidth=0.9, relheight=0.85, relx=0.05, rely=0.03)

btn_container = tk.Frame(root, padx=10, pady=2)
btn_container.pack()

font_family = 'Arial'

open_file = tk.Button(btn_container, 
	text="Open File", 
	padx=18, pady=7, 
	fg="white", 
	bg="#263d42", 
	command=addApp, 
	font=(font_family, 11))

open_file.grid(row=0, column=0)

run_apps = tk.Button(btn_container, 
	text="Run Apps", 
	padx=18, pady=7, 
	fg="white", 
	bg="#263d42", 
	command=runApps, 
	font=(font_family, 11))

run_apps.grid(row=0, column=1)

for app in apps:
	label = tk.Label(frame, text=app)
	label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
	for app in apps:
		f.write(app + ',')
import http.server
import socketserver
import os
import tkinter as tk
from tkinter import Label, Button, Frame
import pystray
from pystray import MenuItem as item, Icon
from PIL import Image, ImageDraw
import threading


PORT = 2100
DIRECTORY = "documentation"


if not os.path.exists(DIRECTORY):
    print(f"Error: The directory '{DIRECTORY}' does not exist.")
    exit(1)

os.chdir(DIRECTORY)
Handler = http.server.SimpleHTTPRequestHandler


def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}\nOpen your browser and visit http://localhost:{PORT}/documentation")
        httpd.serve_forever()


root = tk.Tk()
root.title("YourServer")
root.geometry("500x250")
root.configure(bg="#1E1E1E") 
root.overrideredirect(True) 


title_bar = Frame(root, bg="#333", relief="raised", bd=2, height=30)
title_bar.pack(fill="x", side="top")

title_label = Label(title_bar, text="Your Server", fg="white", bg="#333", font=("Arial", 12, "bold"))
title_label.pack(side="left", padx=10)

def close_app():
    root.quit()
    os._exit(0)

close_button = Button(title_bar, text="✖", fg="white", bg="#444", font=("Arial", 12, "bold"), relief="flat", command=close_app)
close_button.pack(side="right", padx=10)


def start_move(event):
    root.x = event.x
    root.y = event.y

def stop_move(event):
    root.x = None
    root.y = None

def do_move(event):
    x = root.winfo_x() + (event.x - root.x)
    y = root.winfo_y() + (event.y - root.y)
    root.geometry(f"+{x}+{y}")


title_bar.bind("<ButtonPress-1>", start_move)
title_bar.bind("<ButtonRelease-1>", stop_move)
title_bar.bind("<B1-Motion>", do_move)

title_label.bind("<ButtonPress-1>", start_move)
title_label.bind("<ButtonRelease-1>", stop_move)
title_label.bind("<B1-Motion>", do_move)


label = Label(root, text=f"Server running on:\nhttp://localhost:{PORT}\nOpen your browser and visit http://localhost:{PORT}", fg="white", bg="#1E1E1E", font=("Arial", 12))
label.pack(pady=20)


tray_icon = None

def create_tray_icon():
    global tray_icon
    image = Image.new("RGB", (64, 64), (30, 30, 30))
    draw = ImageDraw.Draw(image)
    draw.rectangle((20, 20, 44, 44), fill="black")
    menu = (item("Show", show_window), item("Exit", exit_app))
    tray_icon = Icon("server", image, "Your Server", menu)
    tray_thread = threading.Thread(target=tray_icon.run, daemon=True)
    tray_thread.start()

def show_window(icon, item):
    global tray_icon
    icon.stop()
    root.after(0, root.deiconify)
    tray_icon = None

def exit_app(icon, item):
    icon.stop()
    root.quit()
    os._exit(0)

def hide_to_tray():
    global tray_icon
    root.withdraw()
    if tray_icon is None or not tray_icon.visible:
        create_tray_icon()


button_frame = Frame(root, bg="#1E1E1E")
button_frame.pack(pady=20)

hide_button = Button(button_frame, text="Hide to Tray", command=hide_to_tray, bg="#444", fg="white", font=("Arial", 10), relief="flat", padx=10, pady=5, borderwidth=2)
hide_button.pack(pady=10)

server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

root.mainloop()

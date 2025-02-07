import http.server
import socketserver
import os
import sys
import tkinter as tk
from tkinter import Label, Button, Frame
import pystray
from pystray import MenuItem as item, Icon
from PIL import Image, ImageDraw
import threading
import socket

# Set default port
DEFAULT_PORT = 2100
DIRECTORY = "documentation"

# Check if directory exists, if not, create it
if not os.path.exists(DIRECTORY):
    print(f"Warning: The directory '{DIRECTORY}' does not exist. Creating it now...")
    os.makedirs(DIRECTORY)  # Automatically create the directory

# Function to find an available port
def get_available_port(start_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        while start_port < 65535:
            if s.connect_ex(("localhost", start_port)) != 0:
                return start_port
            start_port += 1
    return None

# Declare PORT as global here
PORT = get_available_port(DEFAULT_PORT)

os.chdir(DIRECTORY)
Handler = http.server.SimpleHTTPRequestHandler

# Function to start the server
def start_server():
    global PORT
    while True:
        try:
            with socketserver.TCPServer(("", PORT), Handler) as httpd:
                httpd.allow_reuse_address = True
                print(f"Serving at http://localhost:{PORT}\nOpen your browser and visit http://localhost:{PORT}")
                httpd.serve_forever()
        except OSError as e:
            print(f"Error: {e}. Retrying with a new port...")
            PORT = get_available_port(PORT + 1)

# Initialize Tkinter
root = tk.Tk()
root.title("YourServer")
root.geometry("500x250")
root.configure(bg="#1E1E1E")
root.overrideredirect(True)

# Title bar
title_bar = Frame(root, bg="#333", relief="raised", bd=2, height=30)
title_bar.pack(fill="x", side="top")

title_label = Label(title_bar, text="Your Server", fg="white", bg="#333", font=("Arial", 12, "bold"))
title_label.pack(side="left", padx=10)

# Close app function
def close_app():
    root.quit()
    os._exit(0)  # Forcefully terminate the application

close_button = Button(title_bar, text="✖", fg="white", bg="#444", font=("Arial", 12, "bold"), relief="flat", command=close_app)
close_button.pack(side="right", padx=10)

# Drag window functions
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

# Server info label
label = Label(root, text=f"Server running on:\nhttp://localhost:{PORT}\nOpen your browser and visit http://localhost:{PORT}",
              fg="white", bg="#1E1E1E", font=("Arial", 12))
label.pack(pady=20)

# System tray icon
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
    os._exit(0)  # Forcefully terminate the application

def hide_to_tray():
    global tray_icon
    root.withdraw()
    if tray_icon is None or not tray_icon.visible:
        create_tray_icon()

# Hide button
button_frame = Frame(root, bg="#1E1E1E")
button_frame.pack(pady=20)

hide_button = Button(button_frame, text="Hide to Tray", command=hide_to_tray, bg="#444", fg="white", font=("Arial", 10),
                      relief="flat", padx=10, pady=5, borderwidth=2)
hide_button.pack(pady=10)

# Start server in a separate thread
server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

root.mainloop()

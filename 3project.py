from tkinter import *
import pyshorteners
import requests

import tkinter as tk

root = tk.Tk()

# Load the PNG image
icon_image = tk.PhotoImage(file='/home/shabnam/Desktop/CodeClause project/logo.png')

# Set the window icon
root.iconphoto(True, icon_image)

root.title('URL Shortener, Branded Short Links & Analytics')
root.geometry("500x500")

def shorten():
    if shorty.get():
        shorty.delete(0, END)

    if my_entry.get():
        # Convert to tinyurl
        url = pyshorteners.Shortener().tinyurl.short(my_entry.get())
        # Output to screen
        shorty.insert(END, url)

def expand():
    short_url = shorty.get()
    if short_url.startswith("http://tinyurl.com/"):
        # Expand TinyURL
        response = requests.head(short_url, allow_redirects=True)
        original_url = response.url
        expanded_url.delete(0, END)
        expanded_url.insert(END, original_url)
    else:
        expanded_url.delete(0, END)
        expanded_url.insert(END, "Not a TinyURL")

my_label = Label(root, text="Enter Link to Shorten", font=("Arial", 24, "bold"), fg="blue")
my_label.pack(pady=20)
my_entry = Entry(root, font=("Arial", 20), width=40, bg="lightgray")
my_entry.pack(pady=20)

my_button = Button(root, text="Shorten Link", command=shorten, font=("Arial", 20, "bold"), fg="green")
my_button.pack(pady=20)

shorty_label = Label(root, text="Shortened Link", font=("Arial", 16), fg="purple")
shorty_label.pack(pady=20)
shorty = Entry(root, font=("Arial", 18), justify=CENTER, width=30, bd=0, bg="lightblue")
shorty.pack(pady=10)

expand_button = Button(root, text="Expand TinyURL", command=expand, font=("Arial", 16), fg="red")
expand_button.pack(pady=10)

expanded_url_label = Label(root, text="Expanded URL", font=("Arial", 16), fg="purple")
expanded_url_label.pack(pady=10)

expanded_url = Entry(root, font=("Arial", 16), justify=CENTER, width=30, bd=0, bg="lightblue")
expanded_url.pack(pady=10)

root.mainloop()
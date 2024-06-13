import tkinter as tk
import customtkinter
from pytube import YouTube
from tkinter import filedialog



def startDownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        tittle.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        
        download_directory = filedialog.askdirectory()
        if download_directory:
            video.download(download_directory)
            finishLabel.configure(text="Downloaded!")
        else:
            finishLabel.configure(text="Download cancelled", text_color="red")
    except Exception as e:
        finishLabel.configure(text="Download error", text_color="red")
       
 
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    # Update progress bar
    progressBar.set(float(percentage_of_completion / 100))


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")


# Adding UI Elements
tittle = customtkinter.CTkLabel(app, text="Insert a YouTube Link")
tittle.pack(padx=10, pady=10)

# Link input
url_var = tk.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress Percentage

pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx = 10, pady= 10)

# Run app
app.mainloop()
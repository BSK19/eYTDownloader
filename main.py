from tkinter import ttk
from ttkthemes import ThemedTk
from pytube import YouTube
from PIL import Image, ImageTk
import requests
from io import BytesIO
from tkinter import filedialog

def display_thumbnail():
    url = url_input.get()
    yt = YouTube(url)

    # Fetch the thumbnail
    response = requests.get(yt.thumbnail_url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))

    # Convert the image for tkinter
    tk_img = ImageTk.PhotoImage(img)

    # Create a label and add the image to it
    thumbnail_label = ttk.Label(image_frame, image=tk_img)
    thumbnail_label.image = tk_img  # keep a reference to the image
    thumbnail_label.grid(column=0, row=0)

def download_video():
    url = url_input.get()
    yt = YouTube(url)
    # Open a dialog box for the user to select a directory
    download_directory = filedialog.askdirectory()
    yt.streams.first().download(output_path=download_directory)
    url_input.delete(0, 'end')

root = ThemedTk(theme="arc")
root.title("eYTDownloader")
root.geometry('1280x720')

# Create a frame for the input and buttons
input_frame = ttk.Frame(root)
input_frame.pack(pady=20)

url_input = ttk.Entry(input_frame, width=40)
url_input.grid(column=0, row=0, padx=10)

thumbnail_button = ttk.Button(input_frame, text="Show Thumbnail", command=display_thumbnail)
thumbnail_button.grid(column=1, row=0, padx=10)

download_button = ttk.Button(input_frame, text="Download Video", command=download_video)
download_button.grid(column=2, row=0, padx=10)

# Create a frame for the image
image_frame = ttk.Frame(root)
image_frame.pack()

root.mainloop()
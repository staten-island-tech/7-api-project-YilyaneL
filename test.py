import tkinter as tk
import tksvg
import requests

def get_svg_from_url(url, scale=1.0):
    # Fetch the SVG content from the URL
    response = requests.get(url)
    response.raise_for_status()  # Ensure the download was successful

    # Use the 'data' parameter to load the SVG string directly
    return tksvg.SvgImage(data=response.text, scale=scale)

root = tk.Tk()

# Example: Loading a public SVG icon
url = "https://assets.ipstack.com/flags/us.svg"
svg_img = get_svg_from_url(url, scale=0.01)

label = tk.Label(root, image=svg_img)
label.pack(padx=20, pady=20)

root.mainloop()

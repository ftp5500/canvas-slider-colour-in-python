import tkinter as tk
window = tk.Tk()

def sliderUpdate(source):
    red = redSlider.get()
    green = greenSlider.get()
    blue = blueSlider.get()
    hexText.delete(0,tk.END)
    hexText.insert(0,colour)

colour = "#CC1111" % (red, green, blue)


redSlider = tk.Scale(window , from_=0 , to = 255 , command = sliderUpdate)
greenSlider = tk.Scale(window , from_=0 , to = 255 , command = sliderUpdate)
blueSlider = tk.Scale(window , from_=0 , to = 255 , command = sliderUpdate)

hexText = tk.Entry(window)

canvas = tk.Canvas(window , height = 400 , width = 400 )
canvas.config(bg=colour)
redSlider.grid(row=1 , column=1)
greenSlider.grid(row = 1 , column = 2)
blueSlider.grid(row=1,column=3)
hexText.grid(row=3 , column = 1 , columnspan = 3)

canvas.grid(row=2,column=1,columnspan=3)
window.mainloop()


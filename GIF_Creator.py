import glob
from importlib.resources import path
from msilib.schema import Extension
from tkinter import *
from tkinter import messagebox
import imageio

def convertToGIF():
    path = direc.get()
    ext = extension.get()
    path_in = path+'/*.'+ext
    path_out = path+'/MyGIF.gif'

    imgs = []
    try:
        file = glob.glob(path_in, recursive=True)
        for im in file:
            imgs.append(imageio.imread(im))
            imageio.mimsave(path_out, imgs, duration= 0.5)
            # messagebox.showinfo('GIF GENERATOR', 'GIF is saved successfully!')
    except:
        messagebox.showinfo('Error occurred!',
                            'check the path of folder or extension of images')

    else:
        messagebox.showinfo('GIF GENERATOR', 'GIF is saved successfully!')


pnl = Tk()
pnl.title('GIF GENERATOR')
pnl.geometry('400x300')
pnl.config(bg='gray')

# Creating the variables to get the path of folder and the extension of images
extension = StringVar(pnl)
direc = StringVar(pnl)

Label(pnl, text='WELCOME', bg='gray', fg='blue',
      font=('Arial', 18, 'bold')).place(x=130)

Label(pnl, text='select the format of image',
      bg='azure', anchor="e", justify=LEFT).place(x=120, y=60)

Radiobutton(pnl, text='png', bg='azure2', variable=extension,
            value='png').place(x=90, y=90)
Radiobutton(pnl, text='jpeg', bg='azure2', variable=extension,
            value='jpeg').place(x=250, y=90)

Label(pnl, text='enter the location that contains images',
      bg='azure2', anchor='e', justify=LEFT).place(x=90, y=135)

Entry(pnl, textvariable=direc, width=34, font=(
    'calibre', 10, 'normal')).place(x=70, y=170)


Button(pnl, text='Proceed', bg='ivory3', font=(
    'calibre', 13), command=convertToGIF).place(x=153, y=220)

pnl.mainloop()

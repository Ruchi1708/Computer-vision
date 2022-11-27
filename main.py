import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk
from Record import record
from inout import visitor
from noise import noise
from work import face_recog


window = tk.Tk()
window.title("Smart cctv for Activity Detection")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('1080x720')

img = tk.PhotoImage(file="bg_wall.png")
frame1 = tk.Frame(window, bg = "grey")

label_title = tk.Label(frame1, text="Smart CCTV")
label_font = font.Font(size=35, weight='bold',family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2)
#label = tk.Label(window, image = img)
#label.place(x=0, y=0)

icon = Image.open('icons/spy.png')
icon = icon.resize((150,150), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5,10), column=2)

btn1_image = Image.open('icons/lamp.png')
btn1_image = btn1_image.resize((50,50), Image.ANTIALIAS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('icons/incognito.png')
btn2_image = btn2_image.resize((50,50), Image.ANTIALIAS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn3_image = Image.open('icons/security-camera.png')
btn3_image = btn3_image.resize((50,50), Image.ANTIALIAS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn4_image = Image.open('icons/rec.png')
btn4_image = btn4_image.resize((50,50), Image.ANTIALIAS)
btn4_image = ImageTk.PhotoImage(btn4_image)

btn5_image = Image.open('icons/exit.png')
btn5_image = btn5_image.resize((50,50), Image.ANTIALIAS)
btn5_image = ImageTk.PhotoImage(btn5_image)

# -----------BUTTON------------
btn_font = font.Font(size=25)
btn1 = tk.Button(frame1, text='Identify', height=90, width=180, fg='green',command = face_recog, image=btn1_image, compound='left')
btn1['font'] = btn_font
btn1.grid(row=3, pady=(20,10), padx=(20,5))

btn2 = tk.Button(frame1, text='Visitor', height=90, width=180, fg='orange', compound='left', image=btn2_image, command = visitor)
btn2['font'] = btn_font
btn2.grid(row=3, pady=(20,10), column=3, padx=(20,5))

btn3 = tk.Button(frame1, text='Noise', height=90, width=180, fg='orange', compound='left', image=btn3_image, command = noise)
btn3['font'] = btn_font
btn3.grid(row=6, pady=(20,10), padx=(20,5))

btn4 = tk.Button(frame1, text = 'Record', height=90, width=180, fg='red', compound = 'left', command= record, image=btn4_image)
btn4['font'] = btn_font
btn4.grid(row=6, pady=(20,10), padx=(20,5), column=3)

btn5 = tk.Button(frame1, height=90, width=180, fg='red', command=window.quit, image=btn5_image)
btn5['font'] = btn_font
btn5.grid(row=8, pady=(20,10), padx=(20,5), column=2)

frame1.pack()
window.mainloop()
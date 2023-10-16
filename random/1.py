import tkinter
import random
def click_btn():
    label["text"] = random.choice(["은미", "정철", "종관", "종현"])
    label.update()
root = tkinter.Tk()
root.title("환일뽑기 프로그램")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
g = tkinter.PhotoImage(file="aaa.png")
canvas.create_image(400, 300, image=g)
label = tkinter.Label(root, text="??", font=("Times New Roman", 120), bg="white")
label.place(x=380, y=60)
button = tkinter.Button(root, text="환일뽑기", font=("Times New Roman", 36), command=click_btn, fg="skyblue")
button.place(x=360, y=400)
root.mainloop()

from tkinter import *

root = Tk()
root.title("projekt - Wiktoria Bobrowska")

root.geometry("400x220")
path=Entry(root, width=60, borderwidth=3)
root.resizable(False, False)

def on_path_click(event):
    path.delete(0, "end")
    path.config(fg="black")

path.insert(0, 'Wpisz ścieżkę do pliku: ')
path.config(fg = 'grey')
path.bind('<FocusIn>', on_path_click)
path.grid(row=0, column=0, columnspan=10, pady=15)
 
def myClick():
    fname=path.get()
    try:
        file=open(fname, 'r')
    except:
        l3=Label(root, text="Nie można otworzyć pliku lub plik nie istnieje!", fg="red").grid(row=5, column=0, columnspan=10, pady=5)

    content=file.read()
    words_in=content.split()

    words=len(words_in) #number of words
    characters=len(content) #number of characters including blank spaces and enters
    #spaces= words - 1 #every blank space is between two words, so if there are n words, there are n-1 blank spaces

    spaces=0
    for char in content:
        if(char == " "):
            spaces+=1 #number of spaces  

    file.close()

    w=Label(root, text=words).grid(row=2, column=1, pady=5, ipadx=0)
    ch=Label(root, text=characters).grid(row=3, column=1, pady=5)
    s=Label(root, text=spaces).grid(row=4, column=1, pady=5)

button1=Button(root, text="Zatwierdź", command=myClick)
button1.grid(row=1, column=0, pady=10, columnspan=30)


l1=Label(root, text="Number of words:").grid(row=2, column=0,pady=5)
l2=Label(root, text="Number of characters: ").grid(row=3, column=0, pady=5)
l3=Label(root, text="Number of spaces: ").grid(row=4, column=0, pady=5)


root.mainloop()
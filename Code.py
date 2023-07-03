from tkinter import *
from translate import Translator

window = Tk()
window.title("Language Translator")
window.geometry("1000x600")
window.config(bg = "white")
 
InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()
LanguageChoices = {'English', 'Hindi', 'Spanish', 'French', 'Greek'}
InputLanguageChoice.set('English')
TranslateLanguageChoice.set('Hindi')

def Translate():
    translator = Translator(from_lang= InputLanguageChoice.get(),to_lang=TranslateLanguageChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)

#create a labelframe
labelframe= LabelFrame(window, text= "Language Traslator", font= ('Century 20 bold'),labelanchor= "n",bd=5,bg= "mintcream",width= 600, height= 450, cursor= "pirate")
labelframe.pack(expand= True, fill= BOTH)

#choice for input language
InputLanguageChoiceMenu = OptionMenu(window,InputLanguageChoice,*LanguageChoices)
Label(width=18, text = 'Choose a Language', relief ='solid', font = 1, bg = 'white', fg = 'green').place(x=100,y=80, height = 40, width = 190)
InputLanguageChoiceMenu.place(x=300,y=80)
InputLanguageChoiceMenu.config(bg = "white", fg= "green", font = 1)
 
#choice in which the language is to be translated
NewLanguageChoiceMenu = OptionMenu(window,TranslateLanguageChoice,*LanguageChoices)
Label(width=18,text="Translated Language", relief= 'solid', font = 0.5 , bg = 'white', fg = 'green', highlightbackground="green", highlightthickness=3).place(x=620,y=80, height = 40, width = 200)
NewLanguageChoiceMenu.place(x=830,y=80)
NewLanguageChoiceMenu.config(bg = "white", fg= "green", font = 1)

Label(width = 10,text="Enter Text", relief = 'ridge', bg = 'white', fg = 'green').place(x=10,y=140)
TextVar = StringVar()
TextBox = Entry(window, textvariable=TextVar, relief = 'ridge', font = 10, highlightbackground="green", highlightthickness=3).place(x=100,y=140, width = 300, height = 250)

 
Label(width = 10,text="Output Text", relief = 'ridge', bg = 'white', fg = 'green').place(x=530,y=140)
OutputVar = StringVar()
TextBox = Entry(window,textvariable=OutputVar, relief = 'ridge', font = 10,  highlightbackground="green", highlightthickness=3).place(x=620,y=140, width = 300, height = 250)
 
#Button for calling function
B = Button(window,text="Translate",command=Translate, relief = 'solid', font = 10, bg = 'white', fg = 'green', highlightbackground="green", highlightthickness=3, bd = 2).place(x=440,y=440, width = 120, height= 40)

window.mainloop()

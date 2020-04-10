#gui
from tkinter import * 

from PyDictionary import PyDictionary 
from tkinter import messagebox  


root = Tk()
root.geometry("250x200")
root.title("Word Dictionary")


def find_meaning():
    word = entry_widget.get() # take user input and store in a variable
    dictionary = PyDictionary() #object of pydictionary
    meaning = dictionary.meaning(word) #returns dictionary if word found else returns none
    #meaning is of dictionary type
    #print(type(meaning))
    #print(meaning)
    string_answer = ""
    
    # using not operator 
    # Check if dictionary is empty  
    res = not meaning  #return true or false
     
    #print("Is dictionary empty ? : " + str(res)) 


    if(res):
        messagebox.showinfo("Result","Sorry No Result Found")
    else:
        for k,v in meaning.items():
            string_answer = string_answer +" \n"+ str(k) + "\n"  + listToString(v) 

        messagebox.showinfo("Result",string_answer)  




def listToString(s): 
    str1 = " " 
    # return string   
    return (str1.join(s)) 
        


entry_widget=Entry(root,font=("times",15,"bold")) 
entry_widget.grid(row=2,column=2)



btn=Button(root,text="Find Meaining",command=find_meaning)
btn.grid(row=4,column=2)

root.mainloop()
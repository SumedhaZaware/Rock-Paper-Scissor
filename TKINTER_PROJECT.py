# Defining the functions used
user_score=0
comp_score=0
user_choice=""
comp_choice=""

def number_to_choice(choice):
    choice_dict={'rock':0,'paper':1,'scissor':2}
    return choice_dict[choice]

def computer_choice():
    return random.choice(["rock","paper","scissor"])

def result(human_choice,comp_choice):
    global user_score
    global comp_score
    choice_user=number_to_choice(human_choice)
    choice_comp=number_to_choice(comp_choice)
    if(choice_user==choice_comp):
        print("Tie")
    elif((choice_user-choice_comp)%3==1):
        print("You win")
        user_score+=1
    else:
        print("Comp wins")
        comp_score+=1
    text_area=Text(win,height=5,width=26)
    text_area.grid(column=1,row=2)
    output="****SCORE BOARD****\nUSER: {uc} \nCOMPUTER: {cc} \nUSER SCORE: {u} \nCOMPUTER SCORE: {c} ".format(uc=user_choice,cc=comp_choice,u=user_score,c=comp_score)    
    text_area.insert(END,output)

def rock():
    global user_choice
    global comp_choice
    user_choice='rock'
    comp_choice=computer_choice()
    result(user_choice,comp_choice)

def paper():
    global user_choice
    global comp_choice
    user_choice='paper'
    comp_choice=computer_choice()
    result(user_choice,comp_choice)

def scissor():
    global user_choice
    global comp_choice
    user_choice='scissor'
    comp_choice=computer_choice() 
    result(user_choice,comp_choice)
   
def About():
    showinfo("Rock-Paper-Scissor","Game by Sumedha Zaware")

def Exit():
    win.destroy()

# Main code for the game
if __name__ == "__main__":
    # Importing modules
    from tkinter import *
    import random
    from tkinter.messagebox import showinfo

    #Setup
    win=Tk()
    win.geometry("1000x1000")
    win.title("ROCK-PAPER-SCISSOR")
    win.iconbitmap('main.ico')

    # Extracting image files
    rock_image=PhotoImage(file="Rock.png")
    paper_image=PhotoImage(file="Paper.png")
    scissor_image=PhotoImage(file="Scissor.png")

    # Creating buttons
    rock_button=Button(command=rock,image=rock_image)
    paper_button=Button(command=paper,image=paper_image)
    scissor_button=Button(command=scissor,image=scissor_image)

    # Packing the buttons
    rock_button.grid(row=0,column=1)
    paper_button.grid(row=0,column=2) 
    scissor_button.grid(row=0,column=3)

    # Menu bar
    MenuBar=Menu(win) 
    OptionBar=Menu(MenuBar,tearoff=0)
    
    # Adding options
    MenuBar.add_cascade(label="Options",menu=OptionBar)
    OptionBar.add_command(label="Exit",command=Exit)
    OptionBar.add_command(label="About",command=About)    

    # Configuring menu bar
    win.config(menu=MenuBar)

    win.mainloop()
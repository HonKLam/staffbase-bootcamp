from tkinter import *
q_list = []
a_list = []

# Question-Screen
def QnA_Home():

    def button_click():
        q = e.get()
        q_list.append(q)
        e.delete(0, END)

    frame = Frame(top)
    frame.pack()

    myLabel = Label(frame, text="Staffbase QnA", font=25)
    myLabel.pack()

    e = Entry(frame, width=20, borderwidth=3)
    e.pack()

    b1 = Button(frame, text = "Submit", command=button_click)
    b1.pack()

    b2 = Button(frame, text = "Show Questions", command=show_list)
    b2.pack()

    return frame

# QuestionList-Screen + Answer Buttons
def show_list():
    qna_frame.destroy()

    global list_frame
    list_frame = Frame(top)
    list_frame.pack()

    i = 0

    for j in range(len(q_list)):
        i += 1
        newLabel = Label(list_frame, width=50, text=q_list[j])
        newLabel.pack()

        q_b = Button(list_frame, text = "Answer Question " + str(i), command=answer_button)
        q_b.pack()


# Answer Screen
def answer_button():
    list_frame.destroy()

    def button_click_2():
        a =  newEntry.get()
        a_list.append(a)
        newEntry.delete(0, END)

    def printAnswers():
        print(a_list)

    global answer_frame
    answer_frame = Frame(top)
    answer_frame.pack()

    new_Label = Label(answer_frame, text=q_list[0])
    new_Label.pack()

    newEntry = Entry(answer_frame)
    newEntry.pack()

    answer_b = Button(answer_frame, text="Submit", command=button_click_2)
    answer_b.pack()

    home_b = Button(answer_frame, text="Back", command=QnA_Home)
    home_b.pack()

    print_b = Button(answer_frame, text="Print out Answers...", command=printAnswers)
    print_b.pack()

    return answer_frame



top = Tk()
top.title("Staffbase QnA")
top.geometry("300x100")

qna_frame = QnA_Home()
qna_frame.pack()

top.mainloop()
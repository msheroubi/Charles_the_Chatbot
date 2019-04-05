import tkinter
import pickle
from os.path import dirname, join
import charles
import convoDemo

current_dir = dirname(__file__)
file_path = join(current_dir, 'question_answers.pickle')
with open(file_path, 'rb') as f:
        question_answers= pickle.load(f)

sub = ""

def send(event=None):  # event is passed by binders.
    global sub
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    if msg == "{quit}" or 'bye' in msg:
        top.quit()
    else:
        msg_list.insert(tkinter.END, ">> "+ msg)
        #response = convoDemo.begin(msg)
        response, sub = charles.getResponse(msg, sub)
        msg_list.insert(tkinter.END, "Charles>> "+ response)

def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.title("Chat On!")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("")
scrollbar = tkinter.Scrollbar(messages_frame)  # To see through previous messages.
# this will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=40, width=120, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

tkinter.mainloop()
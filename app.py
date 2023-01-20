from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:

    def __init__(self):

        self.dbo=Database()

        self.apo=API()
        #login ka gui load karna
        self.root=Tk()
        self.root.title("NLPAPP")
        self.root.geometry("350x600")
        self.root.configure(bg="#34495E")

        self.login_gui()
        self.root.mainloop()



    def login_gui(self):
        # clear the existing gui
        self.clear()

        heading=Label(self.root,text='NLPAPP',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('vendana','24','bold'))

        lebel1=Label(self.root,text="Enter email")
        lebel1.pack(pady=(10,10))

        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(5,5),ipady=4)

        lebel2 = Label(self.root, text="Enter Password")
        lebel2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50,show='*')
        self.password_input.pack(pady=(5, 5),ipady=4)

        login_btn=Button(self.root,text="login",width=30,height=2,command=self.perform_login)
        login_btn.pack(pady=(10,10))

        lebel3 = Label(self.root, text="Not a member?")
        lebel3.pack(pady=(20, 10))

        Redirect_btn = Button(self.root, text="Register Now",command=self.register_gui)
        Redirect_btn.pack(pady=(10, 10))

    def register_gui(self):
        #clear the existing gui
        self.clear()
        heading = Label(self.root, text='NLPAPP', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('vendana', '24', 'bold'))

        lebel0 = Label(self.root, text="Enter Name")
        lebel0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 5), ipady=4)

        lebel1 = Label(self.root, text="Enter email")
        lebel1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 5), ipady=4)

        lebel2 = Label(self.root, text="Enter Password")
        lebel2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 5), ipady=4)

        register_btn = Button(self.root, text="register", width=30, height=2,command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        lebel3 = Label(self.root, text="Already a member?")
        lebel3.pack(pady=(20, 10))

        Redirect_btn = Button(self.root, text="Login Now", command=self.login_gui)
        Redirect_btn.pack(pady=(10, 10))

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        # fetch data from gui
        name=self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        print("inside perform registration")
        response = self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo('success','Registration successfull you can login now')
        else:
            messagebox.showerror('Error','Email id already exists try with new email id')

    def perform_login(self):
        email=self.email_input.get()
        password=self.password_input.get()

        response_new=self.dbo.search(email,password)

        if response_new:
            messagebox.showinfo('success','login succesfull')
            self.home_gui()
        else:
            messagebox.showerror("error",'incorrect email/password')

    def home_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPAPP', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('vendana', '24', 'bold'))

        sentiment_btn = Button(self.root, text="Sentiment Analysis", width=30,height=4,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        NER_btn = Button(self.root, text="Name Entity Recognition",width=30,height=4, command=self.ner_recognition)
        NER_btn.pack(pady=(10, 10))

        Emotion_btn = Button(self.root, text="Emotion Precition", width=30,height=4, command=self.emotion_gui)
        Emotion_btn.pack(pady=(10, 10))

        Logout_btn = Button(self.root, text="logout", command=self.login_gui)
        Logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPAPP', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('vendana', '24', 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('vendana', '20'))

        lebel1 = Label(self.root, text="Enter the text")
        lebel1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=4)
        #
        sentiment_btn = Button(self.root, text="Analyze Sentiment", command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_Result = Label(self.root, text="",bg='#34495E',fg='white')
        self.sentiment_Result.pack(pady=(10, 10))
        self.sentiment_Result.configure(font=('vendana', '16'))

        goback_btn = Button(self.root, text="Go back to home", command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):
        text=self.sentiment_input.get()
        result=self.apo.sentiment_analysis(text)
        #print(result)

        txt=''

        for i in result["sentiment"]:
            txt=txt + i + '-->' + str(result["sentiment"][i]) + '\n'
        self.sentiment_Result["text"]=txt


    def emotion_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPAPP', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('vendana', '24', 'bold'))

        heading2 = Label(self.root, text='Emotion Analysis', bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('vendana', '20'))

        lebel1 = Label(self.root, text="Enter the text")
        lebel1.pack(pady=(10, 10))

        self.emotion_input = Entry(self.root, width=50)
        self.emotion_input.pack(pady=(5, 10), ipady=4)
        #
        emotion_btn = Button(self.root, text="Emotion Prediction", command=self.do_emotion_prediction)
        emotion_btn.pack(pady=(10, 10))

        self.emotion_Result = Label(self.root, text="", bg='#34495E', fg='white')
        self.emotion_Result.pack(pady=(10, 10))
        self.emotion_Result.configure(font=('vendana', '16'))

        goback_btn = Button(self.root, text="Go back to home", command=self.home_gui)
        goback_btn.pack(pady=(8, 8))

    def do_emotion_prediction(self):
        text=self.emotion_input.get()
        result=self.apo.Emotion_recognition(text)
        txt = ''

        for i in result['emotion']:
            txt = txt + i + '-->' + str(result["emotion"][i]) + '\n'
        self.emotion_Result["text"] = txt

    def ner_recognition(self):
        self.clear()
        heading = Label(self.root, text='NLPAPP', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('vendana', '24', 'bold'))

        heading2 = Label(self.root, text='Name Entity Recognition', bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('vendana', '20'))

        lebel1 = Label(self.root, text="Enter the text")
        lebel1.pack(pady=(10, 10))

        self.NER_input = Entry(self.root, width=50)
        self.NER_input.pack(pady=(5, 10), ipady=4)
        #
        NER_btn = Button(self.root, text="Name Entity Prediction", command=self.do_ner_prediction)
        NER_btn.pack(pady=(10, 10))

        self.NER_Result = Label(self.root, text="", bg='#34495E', fg='white')
        self.NER_Result.pack(pady=(10, 10))
        self.NER_Result.configure(font=('vendana', '16'))

        goback_btn = Button(self.root, text="Go back to home", command=self.home_gui)
        goback_btn.pack(pady=(8, 8))

    def do_ner_prediction(self):
        text=self.NER_input.get()
        result=self.apo.NER_recognition(text)

        #print(result)

        txt = ''

        for i in result['entities']:
            txt = txt + str(i) + '\n'
        self.NER_Result["text"] = txt

nlp=NLPApp()


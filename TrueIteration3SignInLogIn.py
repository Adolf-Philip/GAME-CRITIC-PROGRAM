#imports all necessary modules
from tkinter import *
from tkinter import messagebox
import ast
import re




#A try function is over all the code in case of any underlying invalid cases
try:


    ##################################### FUNCTIONS ###################################################

    #---------------------------------------Sign Up------------------------------------------------#
    #The sign up page function contains all the frames, buttons and labels necessary, it contains all the possible function needed within the actual function
    def sign_up_page():

        #Creates all the necessary root requirements for the signup page
        root = Tk()
        root.title("SignUp")
        root.geometry('925x500+300+200')
        root.configure(bg='#fff')
        root.resizable(False, False)

    #---------------------------------------Sign up button pressed-------------------------------#
        def signup():
            
            
            # Gets the Username from entrybox and converts to integer
            username = user.get()
            username = str(username)

            #Checks if Username is Empty
            if username == "":
                messagebox.showerror("Error", "Username cannot be empty")
                user.configure(bg='red')
                code.configure(bg='white')
                confirm_code.configure(bg='white')
                return
            
            if len(username) <= 7:
                messagebox.showerror("Error", "Username must be more than 8 characters long")
                user.configure(bg='red')
                code.configure(bg='white')
                confirm_code.configure(bg='white')
                return

            


            #Gets password from code entrybox
            password = code.get()

            #Password Cannot be left Empty
            if password == "":
                messagebox.showerror("Error in Password", "Password cannot be empty")

            # Password must be more than 8 characters long
            if len(password) < 8:
                messagebox.showerror("Error in Password", "Password must be longer than 8 characters")
                code.configure(bg="red")
                user.configure(bg='white')
                confirm_code.configure(bg='white')
                return

            # Password must contain a number
            elif re.search('[0-9]', password) is None:
                messagebox.showerror("Error in Password", "Password must contain a number")
                code.configure(bg="red")
                user.configure(bg='white')
                confirm_code.configure(bg='white')
                return

            # Password must contain a capital letter
            elif re.search('[A-Z]', code.get()) is None:
                messagebox.showerror("Error in Password", "Password must contain a capital letter")
                code.configure(bg="red")
                user.configure(bg='white')
                confirm_code.configure(bg='white')
                return

            # Password must contain a lowercase letter
            elif re.search('[a-z]', password) is None:
                messagebox.showerror("Error in Password", "Password must contain a lowercase letter")
                code.configure(bg="red")
                user.configure(bg='white')
                confirm_code.configure(bg='white')
                return


            #Gets confirmation of password from confirm_code entrybox
            confirm_password = confirm_code.get()

            #If confirmation of password is same as password
            if password == confirm_password:

                #Converts Username and password back into strings
                username = user.get()
                password = code.get()

                
                    

                #opens database
                file = open('datasheet.txt', 'r+')
                d = file.read()
                r = ast.literal_eval(d)
                

                #makes a dictionary for  username and password
                dict2 = {username: password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                #Adds username id and password
                file = open('datasheet.txt', 'w')
                w = file.write(str(r))
                file.close()

                #Validations are complete and transfers them back to signup page
                messagebox.showinfo('Signup', 'Successful sign up')
                root.destroy()
                login_page()

                

            #Confirm password must be same as password received
            else:
                messagebox.showerror('Invalid', "Both passwords should match")
                code.configure(bg="red")
                confirm_code.configure(bg="red")
                user.configure(bg='white')
                return


        #------------------------------Destroy Window------------------------------#

        #Transfers user back to login_page page
        def sign():
            root.destroy()
            login_page()


        #----------------------------Entry Boxes Startout--------------------------#
        
        #When user is focused on
        def on_enter(e):

            #When empty is displays "Username"
            if user.get() == "Username":
                user.delete(0, 'end')
            
            #Changes background of entrybox to white 
            user.configure(bg='white')


        #When code is focused on
        def on_enter2(e):

            #When empty is displays "Password"
            if code.get() == "Password":
                code.delete(0, 'end')
            
            #Changes background of entrybox to white
            code.configure(bg='white')

    	
        #When the confirmaton of code is focused on
        def on_enter3(e):

            #when empty is displays "Confirm Password"
            if confirm_code.get() == "Confirm Password":
                confirm_code.delete(0, 'end')
            
            #Changes background of entrybox to white
            user.configure(bg='white')


        #When  programmes are not focused on entry boxes
        def on_leave(e):

            #Creates variables for each entrybox
            name = user.get()
            password = code.get()
            confirm_password = confirm_code.get()

            #If Name is "" then it will display Username"
            if name == "":
                user.insert(0, 'Username')

            #If password is "" then it will display "Password"
            elif password == "":
                code.insert(0, 'Password')

            #If confirm_password is "" then it will display "Confirm Password"
            elif confirm_password == "":
                confirm_code.insert(0, "Confirm Password")



        #########################################FRAME#########################################
        frame = Frame(root, width=350, height=390, bg='#fff')
        frame.place(x=480, y=50)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)
        Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)
        Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)



        ##########################################HEADINGS###########################################
        heading = Label(frame, text='Sign up', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
        heading.place(x=100, y=5)



        ##########################################BUTTONS#####################################################
        Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)

        signin1 = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=sign)
        signin1.place(x=200, y=340)



        ##########################################LABELS##############################################################
        label = Label(frame, text='I have an account', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
        label.place(x=90, y=340)



        ############################################USER INPUT#######################################################

        #--------------------------------------------Username------------------------------------------------------#
        user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        user.place(x=30, y=80)
        user.insert(0, 'Username')
        user.bind('<FocusIn>', on_enter)
        user.bind('<FocusOut>', on_leave)


        #--------------------------------------------PASSWORD-------------------------------------------------------#
        code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        code.place(x=30, y=150)
        code.insert(0, 'Password')
        code.bind('<FocusIn>', on_enter2)
        code.bind('<FocusOut>', on_leave)


        #-------------------------------------------CONFIRM CODE---------------------------------------------------#
        confirm_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        confirm_code.place(x=30, y=220)
        confirm_code.insert(0, 'Confirm Password')
        confirm_code.bind('<FocusIn>', on_enter3)
        confirm_code.bind('<FocusOut>', on_leave)



        ############################################ IMAGE ##############################################################
        
        img = PhotoImage(file='signup.png')
        Label(root, image=img, border=0, bg='white').place(x=50, y=100)



        ######################################## ENDS SIGNUP PAGE #######################################################
        root.mainloop()

#------------------------------------------login Page----------------------------------------------#
    #The login page contains all frames, buttons, labels and etc that is necessary, it also includes functions that are needed
    def login_page():

        #Creates all necessary root elements
        root = Tk()
        root.title('login_page')
        root.geometry('925x500+300+200')
        root.configure(bg="#fff")
        root.resizable(False, False)


        ################################# FUNCTIONS ####################################################

        #-------------------------------------- Signup transfering Function ------------------------------------#
        def sign_up_page_transfer():
            root.destroy()
            sign_up_page()


        #-------------------------------Sign in------------------------------------------------------#

        def signin():

            global username
            #Gets the username and password from entryboxes of user and code
            username = user.get()
            password = code.get()

            #Opens datasheet
            file = open('datasheet.txt', 'r')
            d = file.read()
            r = ast.literal_eval(d)
            file.close()

            #if Username and password in datasheet 
            if username in r.keys() and password == r[username]:
                messagebox.showinfo("Welcome back",f"Welcome back {username}")
                root.destroy()
                from TrueIteration3MainPage import main
                
            #Else it displays invalid and returns user to login page
            else:
                messagebox.showerror('Invalid', 'Invalid username or password')
                code.configure(bg='red')
                user.configure(bg='red')


        #-------------------------------------------Entry Boxes Startout---------------------------#
        
        #When user is focused on
        def on_enter(e):

            #When empty is displays "Username"
            if user.get() == "Username":
                user.delete(0, 'end')
            
            #Changes background of entrybox to white 
            user.configure(bg='white')


        #When code is focused on
        def on_enter2(e):

            #When empty is displays "Password" else it removes it
            if code.get() == "Password":
                code.delete(0, 'end')
            
            #Changes background of entrybox to white 
            code.configure(bg='white')


        #When not focused on 
        def on_leave(e):
            
            #Changes entry boxes into variables
            name = user.get()
            password = code.get()

            #If name is empty then it will change to "Username"
            if name == "":
                user.insert(0, 'Username')

            #If password is empty then it will change to "Password"
            elif password == "":
                code.insert(0, 'Password')



        #####################################IMAGE######################################################################
        img = PhotoImage(file='login.png')
        Label(root, image=img, bg='white').place(x=50, y=50)



        ################################################FRAME###############################################################
        frame = Frame(root, width=350, height=350, bg="white")
        frame.place(x=480, y=70)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)
        Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)



        ###################################################HEADINGS###########################################################
        heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=100, y=5)



        #################################################BUTTON#######################################################################
        Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)

        sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=sign_up_page_transfer)
        sign_up.place(x=215, y=270)



        #####################################################LABEL########################################################################
        label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
        label.place(x=75, y=270)



        ######################################################USER INPUT#####################################################################################

        #--------------------------------------------Username---------------------------------------------------------------------------#
        user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        user.place(x=30, y=80)
        user.insert(0, 'Username')
        user.bind('<FocusIn>', on_enter)
        user.bind('<FocusOut>', on_leave)


        #--------------------------------------------PASSWORD-----------------------------------------------------------------------------#
        code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        code.place(x=30, y=150)
        code.insert(0, 'Password')
        code.bind('<FocusIn>', on_enter2)
        code.bind('<FocusOut>', on_leave)



        ################################################ END OF LOGIN PAGE #################################################################################
        root.mainloop()





    #Runs the Login Page
    login_page()





# In case of an unexpected Errors that Occur
except ValueError:
    messagebox.showerror('Error', 'Something went wrong. Please try again later.')

except NameError:
    messagebox.showerror('Error', 'Something went wrong. Please try again later.')

except TypeError:
    messagebox.showerror('Error', 'Something went wrong. Please try again later.')

except BufferError:
    messagebox.showerror('Error', 'Something went wrong. Please try again later.')

except ImportError:
    messagebox.showerror('Error', 'Something went wrong. Please try again later.')
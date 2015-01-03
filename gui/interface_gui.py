__author__ = 'Kelvin Wu'

from Tkinter import *
from ScrolledText import ScrolledText
from easygui import enterbox, buttonbox
import sys

# Setting up the main window and two nested frames
# ====================================================
base = Tk()
base.resizable(width=FALSE, height=FALSE)
base.title("CAMPUS TOOLS by Kelvin Wu")

scrn_height = base.winfo_screenheight()
scrn_width = base.winfo_screenwidth()


def main_position():
    """positions the main window"""
    window_x = 700
    window_y = 315
    base.geometry("{}x{}+{}+{}".format(window_x, window_y,
                                       (scrn_width - window_x) / 2,
                                       (scrn_height - window_y) / 2))

main_window = Frame(base)
main_window.pack(fill=BOTH, expand=1)
main_window.columnconfigure(0, weight=1)
main_window.rowconfigure(0, weight=1)

left_frame = Frame(main_window)
left_frame.grid(row=0, column=0, sticky=N+S+E+W)

right_frame = Frame(main_window)
right_frame.grid(row=0, column=1, sticky=N+S)
# ====================================================


# Some functions for modifying frames
# ====================================================
def clr_frames():
    """clears both frames"""
    for widget in left_frame.winfo_children():
        widget.pack_forget()

    for widget in right_frame.winfo_children():
        widget.pack_forget()


def clr_left():
    """clears left frame (output box)"""
    for widget in left_frame.winfo_children():
        widget.pack_forget()


def clr_right():
    """clears right frame (buttons)"""
    for widget in right_frame.winfo_children():
        widget.pack_forget()


def make_left_scrn(text):
    """creates an instance of the output box with the given
    text"""
    left_scrn = Label(left_frame, text=text, justify=LEFT, anchor=NW,
                      fg="white", bg="black", bd=20, relief=SUNKEN,
                      font="Arial", wraplength=500)
    left_scrn.pack(fill=BOTH, expand=1)


def make_right_button(text, cmd):
    """makes a button with given label and command in the
    right frame"""
    button = Button(right_frame, text=text, width=9, height=2,
                    font="Courier 15 bold", command=cmd)
    button.pack(side=TOP, fill=BOTH)


def make_left_text(text):
    """creates an instance of the output box, but as a text
    widget with scrolling"""
    left_scrn = ScrolledText(left_frame, wrap=WORD, fg="white",
                             bg="black", bd=20, relief=SUNKEN,
                             font="Arial")
    left_scrn.insert(INSERT, text)
    left_scrn.pack(fill=BOTH, expand=1)
# ====================================================


# Using different functions to produce different screens
# ====================================================
def homescreen():
    """creates the main screen"""
    clr_frames()

    make_left_scrn('Welcome to Campus Tools.')

    make_right_button('TUTORS', campustutors)
    make_right_button('FOOD', campusfood)
    make_right_button('WEATHER', campusweather)
    make_right_button('INFO', campusinfo)
    make_right_button('EXIT', sys.exit)
# ====================================================


# Using easygui to get input from the user
# Leaving out a separate screen for this option since it's
# superfluous
# ====================================================
def campustutors():
    """interface for Campus Tutors"""
    course_letter = enterbox('Enter your course abbreviation.')
    if not course_letter:
        return None
    course_number = enterbox('Enter your course number.')
    if not course_number:
        return None

    clr_left()

    if not len(course_letter) <= 5:
        make_left_scrn('Your course abbreviation should '
                       'be no more than five letters.')
    elif not len(course_number) <= 4:
        make_left_scrn('Your course number should '
                       'be less than four digits long.')
    else:
        import tutors_gui

        response = tutors_gui.info_getter(course_letter, course_number)
        if not response:
            make_left_scrn('Sorry, that course is not on the list!')
        else:
            make_left_scrn("Here is the tutor information for your course:\n"
                           "--------------------\n" +
                           response)
# ====================================================


# ====================================================
def campusweather():
    """Campus Weather screen, two options"""
    clr_frames()

    # Defining two local functions to print the info for
    # basic and trivial weather to the output box
    def basicweather():
        import weather_gui

        clr_left()

        make_left_scrn('Here is your weather information ' +
                       '(accurate within 15 minutes):\n' +
                       '--------------------\n' +
                       weather_gui.basic_weather_get())

    def trivialweather():
        import weather_gui

        clr_left()

        make_left_scrn('Here is your weather information ' +
                       '(accurate within 15 minutes):\n' +
                       '--------------------\n' +
                       weather_gui.trivial_weather_get())

    make_left_scrn('Campus Weather. Select your option.')

    make_right_button('BASIC\nWEATHER', basicweather)
    make_right_button('TRIVIAL\nWEATHER', trivialweather)
    make_right_button('RETURN', homescreen)
# ====================================================


# ====================================================
def campusfood():
    """Campus Food screen, three options"""
    clr_frames()

    # Defining the functions for each option
    def what_is_open():
        import menu_gui

        response = menu_gui.open_outlets()

        clr_left()

        if not response:
            make_left_scrn("Sorry, it seems like no one's open right now!")
        else:
            make_left_scrn('These places are open right now:\n' +
                           '--------------------\n' +
                           response +
                           '--------------------')

    def menu_search():
        location = buttonbox('Select the location you are looking up.',
                             '', ['Bon Appetit', 'Festival Fare',
                                  "Mudie's", 'PAS Lounge', 'Pastry Plus',
                                  'REVelations'])
        if not location:
            return None
        day = buttonbox('Select the day you want to check.', '',
                        ['Monday', 'Tuesday', 'Wednesday',
                         'Thursday', 'Friday'])
        if not day:
            return None
        meal = buttonbox("Select the type of meal you're looking for.",
                         '', ['Lunch', 'Dinner'])
        if not meal:
            return None

        import menu_gui
        response = (menu_gui.curr_menu(location, day, meal.lower()))

        clr_left()

        if not response:
            make_left_scrn("Sorry, we couldn't find that outlet's menu!")
        elif response == 'none_day':
            make_left_scrn("Sorry, there is no menu available for that day!")
        elif response == 'none_meal_type':
            make_left_scrn("Sorry, we don't serve that here!")
        else:
            make_left_text('This is the {} {} for {}:\n' +
                           '--------------------\n' +
                           response)

    def nutrition_search():
        try:
            food_id = enterbox('Enter your product ID.')
            if not food_id:
                return None
            else:
                food_id = int(food_id)
                import menu_gui

                response = menu_gui.nutrition_info(food_id)

                clr_left()

                if not response:
                    make_left_scrn("Sorry, we couldn't find that dish!")
                else:
                    make_left_text(response)
        except ValueError:
            clr_left()
            make_left_scrn('Please enter a number.')
            return None

    make_left_scrn('Campus Food. Select your option.')

    make_right_button("WHAT'S\nOPEN?", what_is_open)
    make_right_button('SEARCH\nFOR MENUS', menu_search)
    make_right_button('NUTRITION\nINFO', nutrition_search)
    make_right_button('RETURN', homescreen)
# ====================================================


# ====================================================
def campusinfo():
    """Campus Info screen"""
    clr_frames()

    # Functions
    def employer_infosessions():
        import info_gui

        clr_left()

        make_left_text('Here is a list of upcoming infosessions:\n' +
                       '--------------------\n' +
                       info_gui.sesh_getter())

    def goosewatch():
        import info_gui

        clr_left()

        make_left_text('The geese have taken over these locations:\n' +
                       '--------------------\n' +
                       info_gui.goosewatch())

    make_left_scrn('Campus Info. Select your option.')

    # These buttons have slightly longer labels so they are
    # made custom
    emp_info = Button(right_frame, text='EMPLOYER\nINFOSESSIONS', width=9,
                      height=2, pady=10, font="Courier 11 bold",
                      command=employer_infosessions)
    emp_info.pack(side=TOP, fill=BOTH)
    gw = Button(right_frame, text='GOOSEWATCH', width=9,
                height=2, pady=5, font="Courier 13 bold", command=goosewatch)
    gw.pack(side=TOP, fill=BOTH)
    make_right_button('RETURN', homescreen)
# ====================================================

if __name__ == '__main__':
    main_position()
    homescreen()
    mainloop()
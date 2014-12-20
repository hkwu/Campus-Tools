__author__ = 'Kelvin Wu'

from uwaterlooapi import UWaterlooAPI
import config

uw = UWaterlooAPI(api_key=config.super_secret_key)
tutors = uw.tutors()


# ====================================================
def info_getter(course_letter, course_number):
    """extracts the queried course and its relevant
    tutor information"""
    if not len(course_letter) <= 5:
        print "\nYour course abbreviation should be no more than five letters.\n"
        print "Print press any key to return.\n"
        raw_input("> ")
        import interface
        interface.scrn_clr()
        interface.CampusTutors().__str__()
        interface.CampusTutors().choice()
    elif not len(course_number) <= 4:
        print "\nYour course number should be less than four digits long.\n"
        print "Press any key to return.\n"
        raw_input("> ")
        import interface
        interface.scrn_clr()
        interface.CampusTutors().__str__()
        interface.CampusTutors().choice()
    else:
        for tutor_info in tutors:
            if tutor_info['subject'] == course_letter \
                    and tutor_info['catalog_number'] == course_number:
                print "\n", "-" * 20
                print "Course: {} {} {}\n# of Tutors: {}\nContact: {}" \
                    .format(tutor_info['subject'], tutor_info['catalog_number'],
                            tutor_info['title'], tutor_info['tutors_count'],
                            tutor_info['contact_url']), "\n", "-" * 20, "\n"
                break
        else:
            print "\nSorry, that course is not on the list.\n"
# ====================================================


# ====================================================
def user_enters():
    """gets the user's query"""
    import interface
    interface.CampusTutors().title()
    print "Enter your specifications.\n"
    user_subject = raw_input("Course Abbreviation: ").upper()
    user_catalog = str(raw_input("Course Number: "))
    info_getter(user_subject, user_catalog)
    print "Press any key to return.\n"
    raw_input("> ")
    interface.scrn_clr()
    interface.CampusTutors().__str__()
    interface.CampusTutors().choice()
# ====================================================
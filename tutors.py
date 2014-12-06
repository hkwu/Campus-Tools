__author__ = 'Kelvin Wu'

from uwaterlooapi import UWaterlooAPI

version = 1.0
uw = UWaterlooAPI(api_key="523a61d18c31481685e8957becd8727f")
tutors = uw.tutors()


def info_getter(course_letter, course_number):
    for tutor_info in tutors:
        if tutor_info['subject'] == course_letter \
                and tutor_info['catalog_number'] == course_number:
            print "Course: {0} {1} {2}\n# of Tutors: {3}\nContact: {4}" \
                .format(tutor_info['subject'], tutor_info['catalog_number'],
                        tutor_info['title'], tutor_info['tutors_count'],
                        tutor_info['contact_url'])
            break
    else:
        print "Sorry, that course is not on the list."


def decider(choice):
    user_input = choice.lower()
    if user_input in ['y', 'yes']:
        return True
    elif user_input in ['n', 'no']:
        print "Thanks for using the program."
        return False
    else:
        return decider(raw_input("That is not a valid command. Try again.\n"))

print 'UWaterloo Tutor Finder v{}'.format(version)
init_state = True
while init_state:
    user_subject = raw_input("Enter your subject code.\n").upper()
    while not len(user_subject) <= 5:
        user_subject = raw_input("That is too long. Your subject code should be no more than five letters.\n").upper()
    user_catalog = str(raw_input("Enter your subject number.\n"))
    while not len(user_catalog) == 3:
        user_catalog = str(raw_input("That is invalid. Your subject number should be three digits.\n"))
    info_getter(user_subject, user_catalog)
    init_state = decider(raw_input("Would you like to search for another course?\n"))
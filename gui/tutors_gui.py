__author__ = 'Kelvin Wu'

from uwaterlooapi import UWaterlooAPI
import config

uw = UWaterlooAPI(api_key=config.super_secret_key)
tutors = uw.tutors()


# ====================================================
def info_getter(course_letter, course_number):
    """extracts the queried course and its relevant
    tutor information"""
    for tutor_info in tutors:
        if tutor_info['subject'] == course_letter \
                and tutor_info['catalog_number'] == course_number:
            return ("Course: {} {} {}\n"
                    "# of Tutors: {}\n"
                    "Contact: {}\n"
                    "--------------------") \
                       .format(tutor_info['subject'], tutor_info['catalog_number'],
                               tutor_info['title'], tutor_info['tutors_count'],
                               tutor_info['contact_url'])
    else:
        return False
# ====================================================
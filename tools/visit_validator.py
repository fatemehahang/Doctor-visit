import re
from persiantools.jdatetime import JalaliDateTime

def first_name_validator(first_name):
    if not (type(first_name) == str and re.match(r"^[a-z]{2,30}$", first_name)):
        raise ValueError("Invalid first_name !!!")
    else:
        return first_name

def last_name_validator(last_name):
    if not (type(last_name) == str and re.match(r"^[a-zA-Z\s]{2,30}$", last_name)):
        raise ValueError("Invalid last_name !!!")
    else:
        return last_name

def phone_number_validator(phone_number):
    if not (type(phone_number) == str and re.match(r"^[0-9]{7,14}$", phone_number)):
        raise ValueError("Invalid phone_number !!!")
    else:
        return phone_number
def doctor_name_validator(doctor_name):
    if not (type(doctor_name) == str and re.match(r"^[a-z]{2,30}$", doctor_name)):
        raise ValueError("Invalid doctor_name !!!")
    else:
        return doctor_name

def datetime_validator(date_time):
    if not JalaliDateTime.strptime(date_time, "%Y-%m-%d %H:%M"):
        raise ValueError("Invalid date time format !!!")
    else:
        return date_time

def description_validator(description):
    if not (type(description) == str and re.match(r"^[a-zA-Z\s\d\"\'!?.,:;]{0,30}$", description)):
        raise ValueError("Invalid description !!!")
    else:
        return description
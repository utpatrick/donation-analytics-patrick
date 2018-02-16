import re

def isValidName(name):
    if name == "":
        return False

    pattern = re.compile("\w+,\s\w+")
    if pattern.match(name):
        return True

def isValidZipCode(zipcode):
    if len(zipcode) < 5:
        return False
    return True

def isValidTransDate(date):
    if not date.isdigit() or len(date) != 8:
        return False
    return True

def isValidTransAmount(amount):
    if amount == "" or not amount.isdigit():
        return False
    return True
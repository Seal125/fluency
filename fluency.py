import re


def tripled(l):
    return [n * 3 for n in l]


def only_negative(l):
    return [n for n in l if n < 0]


def total(l):
    return sum(l)


def stripped_strings(l):
    return [re.sub("\W", "", w) for w in l]


def find_lovely(l):
    for i in range(len(l)):
        if l[i] == "lovely":
            return i
    return -1


def valid_contacts(l):
    return [contact for contact in l if len(contact["phone_number"]) == 10]


def contact_names(l):
    return [contact["name"] for contact in l]

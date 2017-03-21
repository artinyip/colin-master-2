from django.test import TestCase
from django.contrib.auth.models import User
from colin_dot_com.models.company import Company, Materials
from colin_dot_com.models.message import Message
from colin_dot_com.services import email_service
import random

COMPANY_FIRST_NAMES = [
    "Superior",
    "Excellent",
    "Kooky",
    "Random",
    "Naughty",
    "Mighty",
    "Jackin'",
    "Sweet",
    "Marvelous"
]

COMPANY_LAST_NAMES = [
    "Wares",
    "Makes",
    "Fixins",
    "Stuff",
    "Works",
    "Things",
    "Shit"
]

COMPANY_TYPES = [
    "Inc",
    "Corps",
    "Corp",
    "& Co",
    "LLC",
    "Brothers"
]

STREET_NAMES = [
    "Main",
    "Bedford",
    "Commerce",
    "Downing",
    "Greene",
    "Metropolitan"
]

STREET_TYPES = [
    "Ave",
    "St",
    "Rd",
    "Ln"
]

CITIES = [
    ["Brooklyn", "NY"],
    ["New York", "NY"],
    ["Philadelphia", "PA"],
    ["Denver", "CO"],
    ["San Francisco", "CA"],
    ["Los Angeles", "CA"],
    ["Dallas", "TX"],
    ["Portland", "OR"],
    ["Boston", "MA"],
    ["Oakland", "CA"],
    ["Chicago", "IL"],
    ["Milwaukee", "WI"]
]

FIRST_NAMES = [
    "John",
    "Jack",
    "Derick",
    "Shawn",
    "Eric",
    "Blane",
    "Mandy",
    "Mindy",
    "Charlotte",
    "Belinda",
    "Shane",
    "Maura",
    "Angela"
]

LAST_NAMES = [
    "Douglas",
    "White",
    "Brown",
    "Miller",
    "Armstong",
    "Angelina",
    "Streeter",
    "Frank",
    "Munn"
]

EMAIL_DOMAINS = [
    "gmailll.com",
    "hotmailll.com",
    "yahoooo.com",
    "zohooo.com",
    "appleee.com"
]


def add_company():
    company = Company()
    company.name = random.choice(COMPANY_FIRST_NAMES) + " " + random.choice(
        COMPANY_LAST_NAMES) + " " + random.choice(COMPANY_TYPES)
    company.material_focus = random.choice(Materials.OPTIONS)
    company.address_line_1 = random.randrange(1, 500).__str__() + " " + random.choice(
        STREET_NAMES) + " " + random.choice(STREET_TYPES)
    city = random.choice(CITIES)
    company.city = city[0]
    company.state = city[1]
    company.blurb = "test"

    firstname = random.choice(FIRST_NAMES)
    lastname = random.choice(LAST_NAMES)
    domain = random.choice(EMAIL_DOMAINS)

    email = firstname + "." + lastname + "@" + domain

    password = "password"

    user = User.objects.create_user(
        username=email,
        email=email,
        first_name=firstname,
        last_name=lastname,
        password=password)

    company.user = user
    company.country = "USA"

    company.save()

    return company

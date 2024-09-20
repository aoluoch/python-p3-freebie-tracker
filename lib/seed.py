#!/usr/bin/env python3

# Script goes here!
from models import Company, Dev, Freebie  # Ensure these imports match your structure
from base import session  # Ensure session is correctly imported

# Create some companies
company1 = Company(name="Tech Corp", founding_year=2000)
company2 = Company(name="Innovate Ltd", founding_year=1995)

# Create some developers
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

# Create some freebies
freebie1 = Freebie(item_name="Mug", value=10, dev=dev1, company=company1)
freebie2 = Freebie(item_name="T-Shirt", value=20, dev=dev2, company=company2)

# Add and commit everything to the database
session.add_all([company1, company2, dev1, dev2, freebie1, freebie2])
session.commit()



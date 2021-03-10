An integration to bring Mautic marketing automation into Django models

**Notice: This is hacky but seems to work fine. If you use this without regular backups on critical infrastructure, you're remarkably daft.**

Confirmed support for Mautic 3 / Django 3.

# Mautic Initial Installation Changes
- Prefix database tables with with crm_
- Install Mautic inside Django MYSQL database

# Installation Instructions
- In settings.py, add 'crm' to INSTALLED_APPS
- I broke views.py so people who don't read the readme will come back and read the notice at the top. Just, like, comment it out or something.
- python manage.py makemigrations
- python manage.py migrate crm --fake

# Usage in Template/View
Used as any other django model: {{ leads.email }} {{ leads.firstname }} {{ leads.lastname }}

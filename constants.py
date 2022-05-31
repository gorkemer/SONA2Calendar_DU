# URL of your SONA system
sona_domain = 'https://du.sona-systems.com/'

# A file that includes your SONA username (on the 1st line) and password (on the 2nd line)
sona_credentials_file = 'sona_credentials.txt'

# Google calendar id (find it in your Calendar Settings -> Calendar ID)
# Make sure the keys in this dictionary match the study names in the SONA system
google_calendar_ids = {'Motion-induced Grouping': 'epk6uuv1fo3a3s6afi2cvo01o4@group.calendar.google.com',
						}

# This dictionary defines the study names to be displayed in the calendar, if different from the study names in SONA.
# Example: {"A long and unclear study name being used in the SONA system": "Short Study Name"}
# Change this to an empty dictionary if you want the study names to be same as in the SONA system
calendar_study_names = {}

# Color scheme for calendar events: if all words (separated by spaces) in a key string of this dictionary can be
# found in the information of a study timeslot, the corresponding color (value in this dictionary) will be applied
# to the calendar event of the study timeslot.
# Example: {'Rm101 Alice': '1', 'Rm102 Alice': '2', 'Rm102 Bob': '3', 'Rm103': '4'}
# For a reference of event colors see https://developers.google.com/google-apps/calendar/v3/reference/colors/get
color_scheme = {'JAC': '2', 'Du': '3', 'Hyon': '4', 'Gharibian': '5'}

# If the researcher has a perferred name (other than their first name) to be shown on the calendar,
# put it in this dictionary.
# The key here should match the researcher name on SONA, the value is their preferred name. 
researcher_names = {'John Chwe': 'JAC'}

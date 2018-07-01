# Tagcounter tutorial project

This simple app was created just as tutorial one.

Application has following functionality:
Application allows to count amount of HTML tags on a certain webpage.
User can start such webpage grabbing with **--get** parameter and appropriate url.
As result of every successful webpage grabbing all elaborated data is saved in sqlite database.
User can restore previously received data from database with **--view** parameter and url as well.
All successful grabbing attempts are logging in dedicated log file.
Application has a file with some abbreviations which can be used instead of urls.
All functionality is accessible from GUI as well.
In order to run application with GUI user shall execute the tagcounter.py script without any parameters.
Otherwise, application will be run in console mode.

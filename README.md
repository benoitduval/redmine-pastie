# redmine-pastie

Installation
============

Manual
------

Go to Package folder (Mac exemple)

    cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages

Clone repository

    git clone git://github.com/benoitduval/redmine-pastie

Reload your Sublime Text application

Add your redmine informations, on the menu go to:

    > Sublime Text > Preferences > Package Settings > Redmine-pastie > Settings - User

Edit file by adding your redmine API key, project name, host and Time-to-live for pastie

    {
        "api_key": "xxxxxx",
        "hostname": "my.redmine.url",
        "project": "myProject",
        "expires": "3600"
    }

Shortcut
--------

By default the shortcut is

    alt+shift+p"

This will paste the selected text (or full file) in Redmine, and set the link in your clipboard
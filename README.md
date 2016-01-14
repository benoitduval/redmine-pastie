# Redmine Pastie

Installation
============

Simply paste your code to the redmine pastie plugin

Using Package Control
---------------------

Open panel with `Cmd+Shift+p`

Launch `Package Control : Add Repository`

Add the link (without .git)

    https://github.com/benoitduval/redmine-pastie

Launch `Package Control : Install Package` and search for `redmine-pastie`

Manual
------

Go to Package folder (Mac exemple)

    cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages

Clone repository

    git clone https://github.com/benoitduval/redmine-pastie.git

Configuration
-------------

Add your redmine informations, on the menu go to:

    > `Sublime Text` > `Preferences` > `Package Settings` > `Redmine-pastie` > `Settings - User`

Edit file by adding your redmine API key, project name, host and Time-to-live for pastie

    {
        "api_key": "xxxxxx",
        "hostname": "my.redmine.url",
        "project": "myProject",
        "expires": "3600"
    }

Shortcut
--------

By default the shortcut is `alt+shift+p`

This will paste the selected text (or full file) in Redmine, and set the link in your clipboard
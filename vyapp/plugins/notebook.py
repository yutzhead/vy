"""
Overview
========

Tabs are a great feature when manipulating several files. This plugin implements Key-Commands to create, 
open files, change the focus between opened tabs.

Usage
=====

The way to create a blank tab is by pressing <F7> in NORMAL mode.    
It will open a new blank tab but keep the focus in the actual one.

There is a handy Key-Command to create a tab and load the contents of a file into it.
For such, just put in NORMAL mode then type <F8>. By pressig <F8> it pops a file
selection window to pick up a file.

Sometimes you will be done with a given tab, you can remove such a tab by pressing <Delete> in
NORMAL mode.

It is possible to change the focus left from a given tab by pressing <Shift-F9>
or changing the focus right by pressing <Shift-F10>. These Key-Commands work regardless
of the mode in which the active AreaVi instance is in. These Key-Commands work on -1 mode.

Key-Commands
============

Mode: NORMAL
Event: <F8>
Description: It pops a file selection window to load the contents of a file in a new tab.

Mode: NORMAL
Event: <F7>
Description: It creates a new blanktab.

Mode: NORMAL
Event: <Delete>
Description: It removes the focused tab.

Mode: -1
Event: <Shift-F9>
Description: It changes the focus left from a tab.

Mode: -1
Event: <Shift-F10>
Description: It changes the focus right from a tab.

"""

from vyapp.app import root
from vyapp.tools import set_status_msg
from tkMessageBox import *
from tkFileDialog import askopenfilename, asksaveasfilename


def load_tab():
    """
    It pops a askopenfilename window to drop
    the contents of a file into another tab's text area.
    """

    filename = askopenfilename()

    # If i don't check it ends up cleaning up
    # the text area when one presses cancel.

    if not filename: 
        return

    try:
        root.note.load([ [filename] ])
    except Exception:
        set_status_msg('It failed to load.')
    else:
        set_status_msg('File loaded.')

def remove_tab():
    """
    It removes the selected tab.
    """

    if len(root.note.tabs()) <= 1: return
    root.note.forget(root.note.select())


def install(area):
    area.install(('NORMAL', '<F8>', lambda event: load_tab()),
                 ('NORMAL', '<F7>', lambda event: root.note.create('None')),
                 ('NORMAL', '<Delete>', lambda event: remove_tab()),
                 (-1, '<Shift-F9>', lambda event: root.note.select(root.note.index(root.note.select()) - 1)),
                 (-1, '<Shift-F10>', lambda event: root.note.select(root.note.index(root.note.select()) + 1)))







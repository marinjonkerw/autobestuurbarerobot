# Handmatige besturing 

# De robot moet vooruit, links, rechts en achteruit kunnen 
# Gevonden op: https://www.daniweb.com/programming/software-development/threads/228595/getting-an-input-from-arrow-keys
# KeyLogger_tk2.py
# show a character key when pressed without using Enter key
# hide the Tkinter GUI window, only console shows

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

def key(event):
    """shows key or tk code for the key"""
    if event.keysym == 'Escape':
        root.destroy()
    if event.keysym == 'Left':
        print( 'Ik ga links') # Dit moet straks aansturing wiel worden
    if event.keysym == 'Up':
        print( 'Ik ga vooruit') # Dit moet straks aansturing wiel worden
    if event.keysym == 'Right':
        print( 'Ik ga rechts') # Dit moet straks aansturing wiel worden
    if event.keysym == 'Down':
        print( 'Ik ga achteruit') # Dit moet straks aansturing wiel worden

root = tk.Tk()
print( "Press a key to ride (Escape key to exit):" )
root.bind_all('<Key>', key)
# don't show the tk window
root.withdraw()
root.mainloop()
'''Creates a very simple UI, which is just a button on a specified shelf containing a popup with all the needed
control shape functions.'''
import maya.cmds as mc


# Local import
import functions
reload(functions)
from __init__ import SHELF_NAME, ICON_PATH

if SHELF_NAME and mc.shelfLayout(SHELF_NAME, ex=1):
    children = mc.shelfLayout(SHELF_NAME, q=1, ca=1) or []
    for each in children:
        try:
            label = mc.shelfButton(each, q=1, l=1)
        except:
            continue
        if label == "ctlShapeManager":
            mc.deleteUI(each)

    mc.setParent(SHELF_NAME)
    mc.shelfButton(l="ctlShapeManager", i="commandButton.png", width=37, height=37, iol="CTL")
    popup = mc.popupMenu(b=1)
    mc.menuItem(p=popup, l="Save to library", c=functions.saveCtlShapeToLib)

    # Build control shapes menu
    sub = mc.menuItem(p=popup, l="Assign from library", subMenu=1)
    for each in functions.getAvailableControlShapes():
        mc.menuItem(p=sub, l=each[0], c=each[1])

    # Build color menu
    sub = mc.menuItem(p=popup, l="Set colour", subMenu=1)
    for each in functions.getAvailableColours():
        mc.menuItem(p=sub, l=each[0], c=each[1], i=ICON_PATH + each[2])

    mc.menuItem(p=popup, divider=True)
    mc.menuItem(p=popup, l="Copy", c=functions.copyCtlShapes)
    mc.menuItem(p=popup, l="Paste", c=functions.pasteCtlShape)
    mc.menuItem(p=popup, l="Copy-Paste", c=functions.copyPasteCtlShape)

    mc.menuItem(p=popup, divider=True)
    mc.menuItem(p=popup, l="Flip", c=functions.flipCtlShape)
    mc.menuItem(p=popup, l="Mirror", c=functions.mirrorCtlShapes)
    mc.menuItem(p=popup, divider=True)
    mc.menuItem(p=popup, l="DELETE", c=functions.deleteCtlShapes)
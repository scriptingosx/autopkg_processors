#!/usr/bin/env python
#
# Copyright 2014 Armin Briegel
#

from Foundation import *



def executeAppleScript(source):
    appleScript = NSAppleScript.alloc().initWithSource_(source)
    print appleScript
    #errorDict = NSMutableDictionary.alloc().initWithCapacity_(10)
    result = appleScript.executeAndReturnError_(objc.NULL)
    return result

script_source = """
    set thepkg to (POSIX file "%s") as alias
    tell application "Remote Desktop"
    	set t to make new install package task with properties {delegating to task server:false, encrypting:true, packages:{thepkg}, stopping on error:false}
    	execute t on computer "%s"
    end tell
"""

pkgpath = "/Users/armin/Library/AutoPkg/Cache/local.pkg.Praat/Praat-5.3.71.pkg"

targetComputerName = "cal-imac05"

scriptresult = executeAppleScript( (script_source % (pkgpath, targetComputerName)) )

print scriptresult

#!/bin/sh

osascript -e \
'tell application "System Events" to tell appearance preferences to set dark mode to true'
defaults -currentHost write -g KeyRepeat -int 2
defaults -currentHost write -g InitialKeyRepeat -int 15
defaults -currentHost write -g com.apple.swipescrolldirection -bool FALSE

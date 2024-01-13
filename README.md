# Hotwheel
This application creates a Circle that serves as an adittional context menu with modular plugin support. The window displays plugins arranged in a circular layout, and plugins can be executed by moving your mouse in the direction of corresponding segment. The intend of this project is to increase productivity, as I feel like this is an crucial missing interaction in my workflow.

# Installation
Download the latest release and run it start.bat 

# Writing a plugin
Use the example plugin as a template for your plugin,

__init__ gets called upon starting the programm
Execute gets called upon triggering the plugin in the context menu

# Customization
If you want to adjust the placement of a plugin in the context menu change the number in the index file in the folder of the plugin, the wheels origin point is 90° 
All other customization options are in the settings.py
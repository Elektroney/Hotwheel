<img src="https://github.com/Elektroney/Hotwheel/assets/54000878/6e69e396-1ed1-4a4a-8e45-531e81011c1e" alt="drawing" width="200"/> 

# Hotwheel
This application creates a Circle that serves as an adittional context menu with modular plugin support. The window displays plugins arranged in a circular layout, and plugins can be executed by moving your mouse in the direction of corresponding segment. The intend of this project is to increase productivity, as I feel like this is an crucial missing interaction in my workflow.

# Installation
Download the latest release and run run.vbs

# Writing a plugin
Use the example plugin as a template for your plugin,

__init__ gets called upon starting the programm  
__Execute__ gets called upon triggering the plugin in the context menu
 <br> After the plugin executes the UI gets reloaded and changes made to the ContextElement get applied 


To install a package to use in your plugin use this command: <br>
"".\bin\python.exe -m pip install --target=.\plugins\libs\  PackageName "" <br>
When uploading your plugin upload the __libs__ folder aswell
 
 Customization
If you want to adjust the placement of a plugin in the context menu change the number in the index file in the folder of the plugin, the wheels origin point is 90° 
All other customization options are in the settings.py

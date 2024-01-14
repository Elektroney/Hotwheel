<img src="https://github.com/Elektroney/Hotwheel/assets/54000878/6e69e396-1ed1-4a4a-8e45-531e81011c1e" alt="drawing" width="200"/> 

# Hotwheel - Additional Context Menu with Modular Plugin Support

Hotwheel is an innovative application designed to create a circular context menu, offering modular plugin support to enhance user interactions. The window displays plugins arranged in a circular layout, allowing users to execute them by moving the mouse in the direction of the corresponding segment. This project aims to fill a crucial missing interaction in the workflow, ultimately boosting productivity.




## Installation
To get started with Hotwheel, follow these simple steps:
1. Download the latest release.
2. Change the activation key to your liking in `settings.py`
3. Run the `run.vbs` script.

  
<br>

## How to Use - Demo

To utilize Hotwheel's functionality, follow these simple steps:

1. Press your activation key 
2. Move your mouse cursor in the direction of the desired function.
3. Release your activation key or mouse button to complete the process.
4. The plugins **\_\_Execute\_\_:** function will get called.

  <img src="https://github.com/Elektroney/Hotwheel/assets/54000878/4cb701e9-8623-46e3-b3c3-fdeee72f16b2" width="300" height="300">
  
<br>  
  
 ## Writing a Plugin
Creating a new plugin for Hotwheel is straightforward. Use the provided example plugin as a template, with the following key functions:

- **\_\_init\_\_:** This function is called upon starting the program.
- **\_\_Execute\_\_:** This function is triggered when the plugin is selected in the context menu.

After a plugin is executed, the user interface reloads, and any changes made to the ContextElement are applied.

To install a package for use in your plugin, execute the following command:

```bash
.\bin\python.exe -m pip install --target=.\plugins\libs\ PackageName
```
Remember to upload the __libs__ folder along with your plugin when sharing. 
## Customization
Adjusting the placement of a plugin in the context menu is possible by changing the number in the index file in the plugin's folder. The wheel's origin point is set at 90°. For additional customization options, refer to the settings.py file.
## Todo
🔲Better looking UI with animations  
🔲Better development qol for installing packages and shipping it as one  
🔲Linux Support 🐧 (Shouldn't be to hard)  

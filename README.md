<img src="https://github.com/Elektroney/Hotwheel/assets/54000878/6e69e396-1ed1-4a4a-8e45-531e81011c1e" alt="drawing" width="200"/> 

# Hotwheel - Additional Context Menu with Modular Plugin Support

Hotwheel is an innovative application designed to create a circular context menu, offering modular plugin support to enhance user interactions. The window displays plugins arranged in a circular layout, allowing users to execute them by moving the mouse in the direction of the corresponding segment. This project aims to fill a crucial missing interaction in the workflow, ultimately boosting productivity.




## Installation
To get started with Hotwheel, follow these simple steps:
1. Download the latest [release](https://github.com/Elektroney/Hotwheel/releases/).
2. Change the activation key to your liking in `settings.py`
3. Run the `run.vbs` script.


## How to Use - Demo

To utilize Hotwheel's functionality, follow these simple steps:

1. Press your activation key 
2. Move your mouse cursor in the direction of the desired function.
3. Release your activation key or mouse button to complete the process.
4. The plugins **\_\_Execute\_\_:** function will get called.

  <img src="https://github.com/Elektroney/Hotwheel/assets/54000878/4cb701e9-8623-46e3-b3c3-fdeee72f16b2" width="300" height="300">
  
<br>  

## Installing a Plugin
1. **Extract the Plugin:**
   If the plugin is in a compressed format (like a zip file), extract its contents to get the plugin folder.

2. **Copy the Plugin:**
   Copy the entire folder of the plugin.

3. **Paste into the "plugins" Folder:**
   Navigate to the root directory of the Hotwheel project and locate the "plugins" folder. Paste the copied plugin folder into this directory.

4. **Adjust the index file**
   If you want to have the plugin appear at a different place on the hotwheel UI change the number inside the index file inside the folder of your plugin incase it doesn't exist create it and change the number to your liking

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

### Support the Project
[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://ko-fi.com/leonkraim)


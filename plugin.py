import os
import importlib
import settings
import logger

plugins = []
stageReinitalization = False
def LoadPlugins():
    global plugins
    plugins = [None for i in range(settings._PLUGIN_ARRAY_SIZE)]

    # Specify the path to the plugins folder
    plugins_folder = 'plugins'

    # Iterate through files in the plugins folder
    for plugin_folder in os.listdir(plugins_folder):
        plugin_path = os.path.join(plugins_folder, plugin_folder)
        if plugin_path == "plugins\\.gitignore":
            continue
        if plugin_path == "plugins\\libs":
            continue
        for plugin_file in os.listdir(plugin_path):
            # Ensure it's a Python file and not a directory
            if plugin_file.endswith('.py') and not plugin_file.startswith('__'):
                # Form the module name by removing the file extension
                module_name = os.path.splitext(plugin_file)[0]

                # Construct the full module path
                module_path = f'{plugins_folder}.{plugin_folder}.{module_name}'

                # Import the module dynamically
                logger.print(module_path)
                module = importlib.import_module(module_path)

                # Assuming there is a class named 'Plugin' in each plugin
                if hasattr(module, 'Plugin') and callable(getattr(module, 'Plugin')):
                    # Create an instance of the Plugin class and add it to the plugins list
                    plugin_instance = getattr(module, 'Plugin')()
                    if(os.path.exists(f"{plugins_folder}\{plugin_folder}\index")):
                        try:
                            plugins[int(open(f"{plugins_folder}\{plugin_folder}\index" ,'r').read())] = plugin_instance
                        except Exception as e:
                            logger.print(str(e)+ "\n\nIndex File Doesnt Contain Index of Plugin :" + plugin_folder )
                    else:   
                    
                        plugins.append(plugin_instance)

def needReinit():
    global stageReinitalization
    toReturn = stageReinitalization
    stageReinitalization = False
    return toReturn

def ExecutePlugin(index):
    global stageReinitalization
    if(index > len(plugins) or plugins[index] == None):
        return
    plugins[index].execute()
    stageReinitalization = True

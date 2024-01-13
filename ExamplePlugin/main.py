import logger

class Plugin:    
    contextElementName = "Execute Example Plugin" 
    def __init__(self):
        logger.print("Example Plugin initialized!")

    def execute(self):
        logger.print("Executing Example Plugin!")

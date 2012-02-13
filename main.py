from settings import Settings
from engine.window import Window
from engine.manager import Manager
from engine.ui import UI

from screens.mainMenu import MenuScreen

window = Window(windowTitle="Shades")

manager = Manager()
window.registerManager(manager)

userInterface = UI(manager)
#screens must be initialized after the manager and the ui
mainScreen = MenuScreen((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT),
                        userInterface)
userInterface.addActiveScreens(mainScreen)

window.run()
window.cleanup()

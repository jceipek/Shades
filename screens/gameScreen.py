#import pymunk as phys

from engine.screen import Screen
from engine.background import Background
from settings import Settings
import dimension

from renderer import CustomRenderer
#from gameObjects.track import Track
#from gameObjects.camera import Camera
#from gameObjects.racer import Racer
from gameObjects.avatar import Avatar

class GameScreen(Screen):

    def __init__(self, size, ui):
        Screen.__init__(self, None, size, ui)
        self.setup()

    def setup(self):
        self.avatar = self.generateAvatar()
        #self.physSpace = self.generatePhysSpace()
        #self.track = self.generateNewTrack()
        #self.racers = self.generateRacers(2)
        #self.cameras = self.generateCameras(2)
        self.renderer = CustomRenderer(imageCache = Screen.imageCache)

        self.renderer.addAvatar(self.avatar)
        #self.renderer.setTrack(self.track)
        #self.renderer.addRacers(self.racers)
        #self.renderer.addCameras(self.cameras)

    def generateAvatar(self):
        avatar = Avatar(dimension.Vect(Settings.SCREEN_WIDTH/2,Settings.SCREEN_HEIGHT/2))
        return avatar


    def initializeCallbackDict(self):
        self.callbackDict = {}
        #self.callbackDict['look'] = ('deviceString', self.steer)
    
        self.callbackDict['exit'] = ('deviceString', self.exit)
        self.callbackDict['p1control_left'] = ('deviceString', self.left)
        self.callbackDict['p1control_right'] = ('deviceString', self.right)

        self.callbackDict['p1control_leftStop'] = ('deviceString', self.leftStop)
        self.callbackDict['p1control_rightStop'] = ('deviceString', self.rightStop)

        self.callbackDict['p1control_jump'] = ('deviceString', self.jump)

    def left(self):
        self.avatar.moveLeft()

    def right(self):
        self.avatar.moveRight()

    def leftStop(self):
        self.avatar.moveLeftStop()

    def rightStop(self):
        self.avatar.moveRightStop()

    def jump(self):
        self.avatar.jump()

    def exit(self):
        self._ui.clearTopScreen()
        #pygame.mixer.music.stop()
    

    def draw(self, surf):
        #Bypasses traditional draw method with renderer
        self.renderer.render()
    
    def update(self, *args):
        gameTime, frameTime = args[:2]

        self.avatar.update(frameTime)

        #for cam, racer in zip(self.cameras,self.racers):
        #    cam.centerOnPt(racer.getPos())
        #dt = 1.0/(Settings.MAX_FPS*20)
        #for x in range(10):
        #    self.physSpace.step(dt)


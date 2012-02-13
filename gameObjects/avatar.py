from settings import Settings
from dimension import Vect
class Avatar:
    """
    The avatar is the player character
    """
    
    def __init__(self, position):
        self.size = Vect(20,20) 
        self.position = Vect(position)
        self.velocity = Vect(0,0)
        self.moveVelocity = Vect(0,0)
        self.moveSpeed = 0.4
        self.jumpSpeed = 1.2
        self.restitution = 0 #0.2
        self.terminalVelocity = 5
        self.acceleration = Vect(0,0)

        self.accumulator = 0.0

        self.oldPos = Vect(0,0)
        self.oldVel = Vect(0,0)
        self.oldAcc = Vect(0,0)

        self.jumpFlag = 0
        self.canDoubleJump = True
        
    def getPos(self):
        return self.position
    
    def getBounds(self):
        return (self.position.x, self.position.y, self.size.x, self.size.y)

    def getPhysPoints(self):
        return self.shape.get_points()
    
    def moveLeft(self):
        self.moveVelocity.x = -self.moveSpeed

    def moveRight(self):
        self.moveVelocity.x = self.moveSpeed

    def moveLeftStop(self):
        if self.moveVelocity.x < 0:
            self.moveVelocity.x = 0

    def moveRightStop(self):
        if self.moveVelocity.x > 0:
            self.moveVelocity.x = 0

    def jump(self):
        if (not self.inAir()) or (self.jumpFlag < 2 and self.canDoubleJump):
            self.moveVelocity.y = -self.jumpSpeed
            self.jumpFlag += 1

    def inAir(self):
        #FIXME
        return (self.position.y < Settings.SCREEN_HEIGHT-100)

    def simulateCollisions(self):
        #FIXME
        if (self.moveVelocity.y+self.velocity.y) > 0 and (self.position.y >= Settings.SCREEN_HEIGHT-100):
            self.jumpFlag = 0
            self.velocity.y = self.restitution*-(self.velocity.y + self.moveVelocity.y)
            if abs(self.velocity.y) < 0.1:
                self.velocity.y = 0
            self.moveVelocity.y = 0
            self.acceleration.y = 0

    def integrate(self, dt):
        if self.inAir():
            self.acceleration.y = 0.003

        self.velocity += dt*self.acceleration

        self.simulateCollisions()

        if self.velocity.y + self.moveVelocity.y > self.terminalVelocity:
            self.position.y += dt*self.terminalVelocity
            self.velocity.y = self.terminalVelocity - self.moveVelocity.y
        elif self.velocity.y + self.moveVelocity.y < -self.terminalVelocity:
            self.position.y += dt*-self.terminalVelocity        
        else:
            self.position += dt*self.moveVelocity
            self.position += dt*self.velocity

    def update(self, frametime):
        dt = 1.0/30.0#60.0

        if frametime > 30.0:
            frametime = 30.0 #avoid spiral of death

        self.accumulator += frametime

        while (self.accumulator >= dt):
            self.oldPos = self.position
            self.oldVel = self.velocity
            self.oldAcc = self.acceleration
            
            self.integrate(dt)
            self.accumulator -= dt

        alpha = self.accumulator/dt

        self.position*alpha + self.oldPos * (1.0-alpha)
        self.velocity*alpha + self.oldVel * (1.0-alpha)
        self.acceleration*alpha + self.oldAcc * (1.0-alpha)


import pygame
import dimension
from renderer import CustomRenderer
from settings import Settings
from gameObjects.track import Track
from gameObjects.camera import Camera
from gameObjects.racer import Racer

if __name__ == "__main__":
    running = True

    renderer = CustomRenderer()

    clock = pygame.time.Clock()

    space = phys.Space()
    space.gravity = (0.0, -900.0)

    racer = Racer(dimension.Vect(Settings.SCREEN_WIDTH/2,Settings.SCREEN_HEIGHT-30))

    track = Track()
    for t in xrange(100):
        track.addSegment(space=space)

    camP1 = Camera( (0,0), (0,                      0,Settings.SCREEN_WIDTH/2,Settings.SCREEN_HEIGHT/2))
    #camP1 = Camera( (0,0), (0,                      0,Settings.SCREEN_WIDTH,Settings.SCREEN_HEIGHT))
    camP2 = Camera( (0,0), (Settings.SCREEN_WIDTH/2,0,Settings.SCREEN_WIDTH/2,Settings.SCREEN_HEIGHT))

    camP3 = Camera( (0,0), (0,                      Settings.SCREEN_HEIGHT/2,Settings.SCREEN_WIDTH/2,Settings.SCREEN_HEIGHT/2))

    camP1.anchorPt.x -= 300

    renderer.setTrack(track)
    renderer.addCamera(camP1)
    renderer.addCamera(camP2)
    renderer.addCamera(camP3)
    renderer.addRacer(racer.shape)

    timeDelta = clock.tick(Settings.MAX_FPS)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        camP1.centerOnPt(racer.getPos())
        camP2.centerOnPt(racer.getPos())
        camP3.centerOnPt(racer.getPos())

        dt = 1.0/600.0
        for x in range(10):
            space.step(dt)

        renderer.render(clock)
        timeDelta = clock.tick(Settings.MAX_FPS)

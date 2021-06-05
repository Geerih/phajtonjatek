import pygame


class Game(object):
    def main(self, screen):

        #load first sprite to image for blit"
        #image = pygame.image.load('')
        #image2 = pygame.image.load('')
        #image3 = pygame.image.load('')
        while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

        screen.fill((200, 200, 200))
        screen.blit(image, (320, 240))
        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    Game().main(screen)
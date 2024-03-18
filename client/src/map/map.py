import pytmx
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600)) # Creates a 800x600 window

tmx_data = pytmx.util_pygame.load_pygame('map.tmx')
for layer in tmx_data.visible_layers:
    if isinstance(layer, pytmx.TiledTileLayer):
        for x, y, gid, in layer:
            tile = tmx_data.get_tile_image_by_gid(gid)
            if tile:
                screen.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))


running = True
while running:
    for event in pygame.event.get():
        pygame.display.update()
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

import os

import pytmx
import pygame
import grpc

from client import Global
from client.src.data.proto_compiled.data import data_pb2_grpc, data_pb2

def show_map():
    print("show_map")
    print(Global.IP)
    print(Global.TOKEN)
    with grpc.insecure_channel(Global.IP) as channel:
        stub = data_pb2_grpc.MapDataStub(channel)
        response = stub.GetMapData(
            data_pb2.GetMapDataRequest(token=Global.TOKEN))

    print(response)
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

if __name__ == '__main__':
    for k in list(os.environ.keys()):
        if k.lower().endswith('_proxy'):
            del os.environ[k]
    show_map()
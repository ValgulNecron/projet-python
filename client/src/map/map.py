import os
import pytmx
import pygame
import grpc
from client.src.entity.entity import play

from client import Global
from client.src.data.proto_compiled.data import data_pb2_grpc, data_pb2

def show_map(root, music_thread, music_manager):
    root.withdraw()  # Hide the current window
    with grpc.insecure_channel(Global.IP) as channel:
        stub = data_pb2_grpc.MapDataStub(channel)
        response = stub.GetMapData(
            data_pb2.GetMapDataRequest(user_id=Global.ID, token=Global.TOKEN))

    # Save the map data to a file
    with open('map.tmx', 'wb') as f:
        f.write(response.map_tmx)
    with open('terrain_atlas.tsx', 'wb') as f:
        f.write(response.terrain_atlas_tsx)
    with open('terrain_atlas.png', 'wb') as f:
        f.write(response.terrain_atlas_png)
    pygame.init()

    screen = pygame.display.set_mode()
    screen_width, screen_height = screen.get_size()
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)


    tmx_data = pytmx.util_pygame.load_pygame('map.tmx')
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid, in layer:
                tile = tmx_data.get_tile_image_by_gid(gid)
                if tile:
                    screen.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))
    play(screen,tmx_data)

    # Remove the map data file
    os.remove('map.tmx')
    os.remove('terrain_atlas.tsx')
    os.remove('terrain_atlas.png')
    pygame.quit()
    root.deiconify()  # Show the window
    music_manager.stop_music()
    import client.src.client.AccountInfoUI as AccountInfoUI
    AccountInfoUI.account_info_ui(root)  # Call the account_info_ui function with the root window


if __name__ == '__main__':
    for k in list(os.environ.keys()):
        if k.lower().endswith('_proxy'):
            del os.environ[k]
    show_map()

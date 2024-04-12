import random

import grpc
import pygame
import pytmx

from client import Global
from client.src.entity.proto_compiled.entity import player_pos_pb2, player_pos_pb2_grpc
from client.src.entity.proto_compiled.entity.player_pos_pb2 import Pos, UpdatePosRequest


def play(screen, tmx_data):
    # Camera variables
    cameraX = 0
    cameraY = 0

    # Base Entity Class
    class Entity(pygame.sprite.Sprite):
        def __init__(self, image_path, x, y):
            super().__init__()
            self.image = pygame.image.load(image_path)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    # Player Class
    class Player(Entity):
        def __init__(self, image_path, x, y):
            super().__init__(image_path, x, y)

        def draw(self, screen):
            # Adjust the entity's position based on the camera's position
            screen.blit(self.image, (self.rect.x - cameraX, self.rect.y - cameraY))

        def move(self, x, y, other_players):
            self.rect.x += x
            self.rect.y += y
            for other_player in other_players:
                new_x = other_player.rect.x
                new_y = other_player.rect.y
                new_x -= x
                new_y -= y
                other_player.move(new_x, new_y)
    # Monster Class
    class Monster(Entity):
        def __init__(self, image_path, x, y):
            super().__init__(image_path, x, y)
            self.direction = 0  # 0: left, 1: right, 2: up, 3: down
            self.steps = 32  # Number of steps in each direction

        def move(self, player_x_movement, player_y_movement):
            # Move the monster in a square pattern
            direction_list = ((-1, 0), (1, 0), (0, -1), (0, 1))
            dx, dy = direction_list[self.direction]
            next_x = self.rect.x + dx
            next_y = self.rect.y + dy
            # counteract player movement
            next_x -= player_x_movement
            next_y -= player_y_movement

            # Check for collisions with collision_objects
            next_rect = pygame.Rect(next_x, next_y, self.rect.width, self.rect.height)
            for obj_rect in collision_objects:
                if next_rect.colliderect(obj_rect):
                    return  # Do not move if the next position would collide with a collision_object

            # Check for collisions with other monsters
            collide = False
            for wall in monsters:
                if wall != self and wall.rect.colliderect(next_rect):
                    collide = True
                    break

            if not collide:
                self.rect.x = next_x
                self.rect.y = next_y

            self.steps -= 1
            if collide or self.steps == 0:
                # Change direction and reset steps
                self.direction = (self.direction + 1) % 4  # Move in a square pattern
                self.steps = 32

        def draw(self, screen):
            # Draw the monster at a fixed position on the screen
            screen.blit(self.image, (self.rect.x, self.rect.y))

    class OtherPlayer(Entity):
        def __init__(self, image_path, x, y, id):
            self.id = id
            super().__init__(image_path, x, y)

        def draw(self, screen):
            # Draw the monster at a fixed position on the screen
            screen.blit(self.image, (self.rect.x, self.rect.y))

        def move(self, new_x, new_y):
            self.rect.x = new_x
            self.rect.y = new_y


    # ... rest of the class ...
    # Spawn the player on a fixed tile
    player = Player('Player.png', 400, 300)  # Example fixed position
    other_players = pygame.sprite.Group()
    # get other player position
    with grpc.insecure_channel(Global.IP) as channel:
        stub = player_pos_pb2_grpc.PlayerPosServiceStub(channel)
        response = stub.PlayerGetAllPos(player_pos_pb2.GetPosRequest(user_id=Global.ID, token=Global.TOKEN))
    for pos in response.pos:
        pos = pos.pos
        player2 = Player('Player.png', pos.pos_x, pos.pos_y)
        other_players.add(player2)
    # Spawn monsters randomly within the map bounds
    monsters = pygame.sprite.Group()
    for _ in range(10):  # Spawn 10 monsters
        x = random.randint(0, tmx_data.width * tmx_data.tilewidth)
        y = random.randint(0, tmx_data.height * tmx_data.tileheight)
        i = random.randint(1, 4)
        if i == 1:
            monster = Monster('monstre1.png', x, y)
        if i == 2:
            monster = Monster('monstre2.png', x, y)
        if i == 3:
            monster = Monster('monstre3.png', x, y)
        if i == 4:
            monster = Monster('monstre4.png', x, y)
        monsters.add(monster)

    # Create a group for players
    all_players = pygame.sprite.Group()
    all_players.add(player)

    import threading
    running = True

    def get_other_players():
        other_players.empty()
        while running:
            with grpc.insecure_channel(Global.IP) as channel:
                stub = player_pos_pb2_grpc.PlayerPosServiceStub(channel)
                response = stub.PlayerGetAllPos(player_pos_pb2.GetPosRequest(user_id=Global.ID, token=Global.TOKEN))
            print(response)
            # remove from the list the player that is currently playing (with the same id as the current player)
            for player in response.pos:
                if player.user_id == Global.ID:
                    continue
                elif player.user_id != Global.ID:
                    # check if the player is already in the list
                    already_in_list = False
                    for other_player in other_players:
                        if other_player.id == player.user_id:
                            already_in_list = True
                            pos = player.pos
                            other_player.move(pos.pos_x, pos.pos_y)
                            break
                    if not already_in_list:
                        pos = player.pos
                        player2 = OtherPlayer('Player.png', pos.pos_x, pos.pos_y, player.user_id)
                        other_players.add(player2)

            # make the thread sleep for 1 second
            player_x_movement_for_other = 0
            player_y_movement_for_other = 0
            threading.Event().wait(1)

    # Create a new thread and start it
    thread = threading.Thread(target=get_other_players)
    thread.start()

    def update_pos(player_x, player_y):
        with grpc.insecure_channel(Global.IP) as channel:
            stub = player_pos_pb2_grpc.PlayerPosServiceStub(channel)
            pos = Pos(pos_x=player_x, pos_y=player_y, last_update=0)
            player_pos = UpdatePosRequest(user_id=Global.ID, token=Global.TOKEN, pos=pos)
            response = stub.PlayerUpdatePos(player_pos)

    # Game Loop
    compteur = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Clear the screen
        screen.fill((0, 0, 0))

        # Initialize collision_objects list
        collision_objects = []

        # Populate collision_objects with objects marked for collision
        for layer in tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledObjectGroup):
                for obj in layer:
                    if obj.properties.get('collision', False):
                        obj_rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                        collision_objects.append(obj_rect)

        # load the collision objects
        for obj_rect in collision_objects:
            pygame.draw.rect(screen, (255, 0, 0), obj_rect.move(-cameraX, -cameraY), 2)
            # add a border around the collision objects

        # Update camera position based on player's position
        cameraX = player.rect.x - screen.get_width() // 2
        cameraY = player.rect.y - screen.get_height() // 2

        # Draw the map
        for layer in tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        screen.blit(tile, (x * tmx_data.tilewidth - cameraX, y * tmx_data.tileheight - cameraY))

        # Draw the player and monsters
        player.draw(screen)
        for monster in monsters:
            monster.draw(screen)
        for other_player in other_players:
            other_player.draw(screen)
        # Update the display
        pygame.display.flip()

        # Player movement based on keyboard input
        keys = pygame.key.get_pressed()
        player_x_movement, player_y_movement = 0, 0
        if keys[pygame.K_LEFT]:
            player_x_movement -= 5
        if keys[pygame.K_RIGHT]:
            player_x_movement += 5
        if keys[pygame.K_UP]:
            player_y_movement -= 5
        if keys[pygame.K_DOWN]:
            player_y_movement += 5

        player.move(player_x_movement, player_y_movement, other_players)

        # Check for collisions with collision_objects
        player_rect = pygame.Rect(player.rect.x, player.rect.y, player.rect.width, player.rect.height)
        for obj_rect in collision_objects:
            if player_rect.colliderect(obj_rect):
                # Handle collision here
                a = a

        # Monster movement
        for monster in monsters:
            monster.move(player_x_movement, player_y_movement)

        # Check for collisions between players
        collisions = pygame.sprite.groupcollide(all_players, all_players, False, False)
        for player, collided_players in collisions.items():
            # Handle collision logic here
            a = 2


        # update pos to server
        compteur += 1
        if compteur == 10:
            player_x = player.rect.x
            player_y = player.rect.y
            thread = threading.Thread(target=update_pos, args=(player_x, player_y))
            thread.start()
            compteur = 0

    pygame.quit()


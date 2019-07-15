import pygame
import math
import os
import easygui

#Define colors.
color_black = (20, 12, 28)
color_purple = (68, 36, 52)
color_dark_blue = (48, 52, 109)
color_dark_gray = (78, 74, 78)
color_brown = (133, 76, 48)
color_dark_green = (52, 101, 36)
color_red = (208, 70, 72)
color_gray = (117, 113, 97)
color_blue = (89, 125, 206)
color_orange = (210, 125, 44)
color_light_gray = (133, 149, 161)
color_light_green = (109, 170, 44)
color_peach = (210, 170, 153)
color_light_blue = (109, 194, 202)
color_yellow = (218, 212, 94)
color_white = (222, 238, 214)
color_transparent = (255, 0, 255)

#This function returns the color of an id from the sprite string.
def get_color(character):
    
    if character == '1':
        return color_black
    if character == '2':
        return color_purple
    if character == '3':
        return color_dark_blue
    if character == '4':
        return color_dark_gray
    if character == '5':
        return color_brown
    if character == '6':
        return color_dark_green
    if character == '7':
        return color_red
    if character == '8':
        return color_gray
    if character == '9':
        return color_blue
    if character == '0':
        return color_orange
    if character == 'a':
        return color_light_gray
    if character == 'b':
        return color_light_green
    if character == 'c':
        return color_peach
    if character == 'd':
        return color_light_blue
    if character == 'e':
        return color_yellow
    if character == 'f':
        return color_white
    if character == 'g':
        return color_transparent

#This function returns the id of a color variable.
def get_color_id(color):
    
    if color == color_black:
        return '1'
    if color == color_purple:
        return '2'
    if color == color_dark_blue:
        return '3'
    if color == color_dark_gray:
        return '4'
    if color == color_brown:
        return '5'
    if color == color_dark_green:
        return '6'
    if color == color_red:
        return '7'
    if color == color_gray:
        return '8'
    if color == color_blue:
        return '9'
    if color == color_orange:
        return '0'
    if color == color_light_gray:
        return 'a'
    if color == color_light_green:
        return 'b'
    if color == color_peach:
        return 'c'
    if color == color_light_blue:
        return 'd'
    if color == color_yellow:
        return 'e'
    if color == color_white:
        return 'f'
    if color == color_transparent:
        return 'g'

def main():
    
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.display.set_caption("Sprite/Tile Editor")
    screen = pygame.display.set_mode((736, 576))
    font = pygame.font.Font('bin/FreeMono.ttf', 16)
    
    #Pre-render text
    text_transparent = font.render('Transparent', False, color_white)
    text_transparent_rect = text_transparent.get_rect()
    text_transparent_rect.center = (640, 176)
    text_animated = font.render('Un-Animate', False, color_white)
    text_animated_rect = text_animated.get_rect()
    text_animated_rect.center = (640, 7*32 + 16)
    text_animated_not = font.render('Animate', False, color_white)
    text_animated_not_rect = text_animated_not.get_rect()
    text_animated_not_rect.center = (640, 7*32 + 16)
    text_frame_one = font.render('Frame One', False, color_white)
    text_frame_one_rect = text_frame_one.get_rect()
    text_frame_one_rect.center = (640, 8*32 + 16)
    text_frame_two = font.render('Frame Two', False, color_white)
    text_frame_two_rect = text_frame_two.get_rect()
    text_frame_two_rect.center = (640, 8*32 + 16)
    text_new_sprite = font.render('New Sprite', False, color_white)
    text_new_sprite_rect = text_new_sprite.get_rect()
    text_new_sprite_rect.center = (640, 430)
    text_new_tileset = font.render('New Tileset', False, color_white)
    text_new_tileset_rect = text_new_tileset.get_rect()
    text_new_tileset_rect.center = (640, 462)
    text_save = font.render('Save', False, color_white)
    text_save_rect = text_save.get_rect()
    text_save_rect.center = (640, 494)
    text_load = font.render('Load', False, color_white)
    text_load_rect = text_load.get_rect()
    text_load_rect.center = (640, 526)
    
    #Set up variables here.
    color_selected = color_white
    #Variables for sprites.
    blank_sprite = 'gggggggggggggggg' \
                   + 'gggggggggggggggg' \
                   + 'gggggggggggggggg' \
                   + 'gggggggggggggggg' \
                   + 'gggggggggggggggg' \
                   + 'gggggggggggggggg' \
                   + 'gggggggggggggggg' \
                   + 'gggggggggggggggg' \
                   + 'gggggggggggggggg' \
                   + 'gggggggggggggggg' \
                   + 'gggggggggggggggg' \
                   + 'gggggggggggggggg' \
                   + 'gggggggggggggggg' \
                   + 'gggggggggggggggg' \
                   + 'gggggggggggggggg' \
                   + 'gggggggggggggggg'
    loaded_sprite = blank_sprite
    image_type = ''
    image_animated = 'false'
    image_frame = 1
    unloaded_sprite = loaded_sprite
    #Variables for tilesets.
    tiles = 16
    tile = 1
    blank_tileset = ['']*16
    while tile <= tiles:
        blank_tileset[tile-1] = blank_sprite
        tile += 1
    loaded_tileset = blank_tileset[:]
    selected_tile = 1
    
    #This is the start of the main program loop.
    clock = pygame.time.Clock()
    running = True
    while running:
        
        #Handle any sort of user input.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or \
                   event.key == pygame.K_LEFTBRACKET:
                    if image_animated == 'true':
                        if image_frame == 2:
                            image_frame = 1
                            buffer_sprite = loaded_sprite
                            loaded_sprite = unloaded_sprite
                            unloaded_sprite = buffer_sprite
                if event.key == pygame.K_RIGHT or \
                   event.key == pygame.K_RIGHTBRACKET:
                    if image_animated == 'true':
                        if image_frame == 1:
                            image_frame = 2
                            buffer_sprite = loaded_sprite
                            loaded_sprite = unloaded_sprite
                            unloaded_sprite = buffer_sprite
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Convert the mouse coordinates to our x/y grid.
                mouse_x, mouse_y = pygame.mouse.get_pos()
                mouse_x = int(math.floor(mouse_x/32))
                mouse_y = int(math.floor(mouse_y/32))
                
                #Deal with click in sprite edit area.
                #Replaced by the click/hold/draw function.
                #Remove after more testing.
                '''if mouse_x >= 1 and mouse_x <= 16 \
                   and mouse_y >=1 and mouse_y <= 16 and image_type != '':
                    #If the mouse is in bounds, apply the color to the sprite.
                    pixel = (mouse_y*16 -16) + mouse_x
                    loaded_sprite = loaded_sprite[:pixel-1] + \
                                    get_color_id(color_selected) + \
                                    loaded_sprite[pixel:]
                    loaded_tileset[selected_tile-1] = loaded_sprite'''
                    
                #Deal with click in color palette.
                if mouse_x == 18 and mouse_y == 1:
                    color_selected = color_black
                if mouse_x == 19 and mouse_y == 1:
                    color_selected = color_purple
                if mouse_x == 20 and mouse_y == 1:
                    color_selected = color_dark_blue
                if mouse_x == 21 and mouse_y == 1:
                    color_selected = color_dark_gray
                if mouse_x == 18 and mouse_y == 2:
                    color_selected = color_brown
                if mouse_x == 19 and mouse_y == 2:
                    color_selected = color_dark_green
                if mouse_x == 20 and mouse_y == 2:
                    color_selected = color_red
                if mouse_x == 21 and mouse_y == 2:
                    color_selected = color_gray
                if mouse_x == 18 and mouse_y == 3:
                    color_selected = color_blue
                if mouse_x == 19 and mouse_y == 3:
                    color_selected = color_orange
                if mouse_x == 20 and mouse_y == 3:
                    color_selected = color_light_gray
                if mouse_x == 21 and mouse_y == 3:
                    color_selected = color_light_green
                if mouse_x == 18 and mouse_y == 4:
                    color_selected = color_peach
                if mouse_x == 19 and mouse_y == 4:
                    color_selected = color_light_blue
                if mouse_x == 20 and mouse_y == 4:
                    color_selected = color_yellow
                if mouse_x == 21 and mouse_y == 4:
                    color_selected = color_white
                if mouse_x >= 18 and mouse_x <= 21 and mouse_y == 5:
                    color_selected = color_transparent
                    
                #Deal with click on tileset preview if visible.
                if image_type == 'tileset':
                    if mouse_x == 18 and mouse_y == 7:
                        selected_tile = 1
                        loaded_sprite = loaded_tileset[selected_tile-1]
                    if mouse_x == 19 and mouse_y == 7:
                        selected_tile = 2
                        loaded_sprite = loaded_tileset[selected_tile-1]
                    if mouse_x == 20 and mouse_y == 7:
                        selected_tile = 3
                        loaded_sprite = loaded_tileset[selected_tile-1]
                    if mouse_x == 21 and mouse_y == 7:
                        selected_tile = 4
                        loaded_sprite = loaded_tileset[selected_tile-1]
                    if mouse_x == 18 and mouse_y == 8:
                        selected_tile = 5
                        loaded_sprite = loaded_tileset[selected_tile-1]
                    if mouse_x == 19 and mouse_y == 8:
                        selected_tile = 6
                        loaded_sprite = loaded_tileset[selected_tile-1]
                    if mouse_x == 20 and mouse_y == 8:
                        selected_tile = 7
                        loaded_sprite = loaded_tileset[selected_tile-1]
                    if mouse_x == 21 and mouse_y == 8:
                        selected_tile = 8
                        loaded_sprite = loaded_tileset[selected_tile-1]
                    if mouse_x == 18 and mouse_y == 9:
                        selected_tile = 9
                        loaded_sprite = loaded_tileset[selected_tile-1]
                    if mouse_x == 19 and mouse_y == 9:
                        selected_tile = 10
                        loaded_sprite = loaded_tileset[selected_tile-1]
                    if mouse_x == 20 and mouse_y == 9:
                        selected_tile = 11
                        loaded_sprite = loaded_tileset[selected_tile-1]
                    if mouse_x == 21 and mouse_y == 9:
                        selected_tile = 12
                        loaded_sprite = loaded_tileset[selected_tile-1]
                    if mouse_x == 18 and mouse_y == 10:
                        selected_tile = 13
                        loaded_sprite = loaded_tileset[selected_tile-1]
                    if mouse_x == 19 and mouse_y == 10:
                        selected_tile = 14
                        loaded_sprite = loaded_tileset[selected_tile-1]
                    if mouse_x == 20 and mouse_y == 10:
                        selected_tile = 15
                        loaded_sprite = loaded_tileset[selected_tile-1]
                    if mouse_x == 21 and mouse_y == 10:
                        selected_tile = 16
                        loaded_sprite = loaded_tileset[selected_tile-1]
                    
                #Deal with click on animate button if visible.
                if image_type == 'sprite' and mouse_x >= 18 and \
                   mouse_x <= 21 and mouse_y == 7:
                    if image_animated == 'true':
                        if easygui.ccbox( \
                            'Are you sure you want to remove the animation?'):
                            image_animated = 'false'
                            easygui.msgbox('Removed other frame.')
                    else:
                        image_animated = 'true'
                        unloaded_sprite = loaded_sprite
                        easygui.msgbox('Created second frame for animation.')
                #Deal with click on the frame change button if visible.
                if image_type == 'sprite' and mouse_x >= 18 and \
                   mouse_x <= 21 and mouse_y == 8:
                    if image_animated == 'true':
                        if image_frame == 1:
                            image_frame = 2
                        else:
                            image_frame = 1
                        buffer_sprite = loaded_sprite
                        loaded_sprite = unloaded_sprite
                        unloaded_sprite = buffer_sprite
                        
                #Deal with click on the New Sprite button.
                if (mouse_x == 18 \
                    or mouse_x == 19 \
                    or mouse_x == 20 \
                    or mouse_x == 21) \
                    and mouse_y == 13:
                        #Create a new sprite if they confirm.
                        if easygui.ccbox( \
                            'Are you sure you want to create a new sprite?'):
                            image_type = 'sprite'
                            image_animated = 'false'
                            loaded_sprite = blank_sprite
                            
                #Deal with click on the New Tileset button.
                if (mouse_x == 18 \
                    or mouse_x == 19 \
                    or mouse_x == 20 \
                    or mouse_x == 21) \
                    and mouse_y == 14:
                        #Create a new tileset if they confirm.
                        if easygui.ccbox( \
                            'Are you sure you want to create a new tileset?'):
                            image_type = 'tileset'
                            image_animated = 'false'
                            loaded_tileset = blank_tileset[:]
                            loaded_sprite = blank_sprite
                            selected_tile = 1
                            
                #Deal with click on the Save button.
                if (mouse_x == 18 \
                    or mouse_x == 19 \
                    or mouse_x == 20 \
                    or mouse_x == 21) \
                    and mouse_y == 15:
                        #Save image to file.
                        file_path = easygui.filesavebox(None, None, '*.gfx')
                        if file_path != None:
                            file = open(file_path, 'w')
                            if image_type == 'sprite':
                                file.write(image_type + '\n' + \
                                           image_animated + '\n' + \
                                           loaded_sprite)
                                if image_animated == 'true':
                                    file.write('\n' + unloaded_sprite)
                            if image_type == 'tileset':
                                file.write(image_type + '\n' + \
                                           image_animated + '\n')
                                tile = 1
                                while tile <= 16:
                                    file.write(loaded_tileset[tile-1] + '\n')
                                    tile += 1
                            file.close()
                            easygui.msgbox('File saved as ' + file_path + '.')
                            
                #Deal with click on the Load button.
                if (mouse_x == 18 \
                    or mouse_x == 19 \
                    or mouse_x == 20 \
                    or mouse_x == 21) \
                    and mouse_y == 16:
                        #Load image from file.
                        file_path = easygui.fileopenbox(None, None, '*.gfx')
                        if file_path != None:
                            file = open(file_path, 'r')
                            image_type = file.readline().replace('\n', '')
                            image_animated = file.readline().replace('\n', '')
                            if (image_type == 'sprite'):
                                loaded_sprite = \
                                              file.readline().replace('\n', '')
                                if (image_animated == 'true'):
                                    unloaded_sprite = \
                                                    file.readline().replace( \
                                                        '\n', '')
                            if (image_type == 'tileset'):
                                tile = 1
                                while tile <= 16:
                                    loaded_tileset[tile-1] = file.readline().\
                                                             replace('\n', '')
                                    tile += 1
                            easygui.msgbox('Loaded file ' + file_path + '.')
                            file.close()
        #Deal with the mouse button being held down in the sprite area.
        mouse_state = pygame.mouse.get_pressed()
        if mouse_state[0] == 1:
            #Convert the mouse coordinates to our x/y grid.
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_x = int(math.floor(mouse_x/32))
            mouse_y = int(math.floor(mouse_y/32))
            
            #Deal with click in sprite edit area.
            if mouse_x >= 1 and mouse_x <= 16 \
               and mouse_y >=1 and mouse_y <= 16 and image_type != '':
                #If the mouse is in bounds, apply the color to the sprite.
                pixel = (mouse_y*16 -16) + mouse_x
                loaded_sprite = loaded_sprite[:pixel-1] + \
                                get_color_id(color_selected) + \
                                loaded_sprite[pixel:]
                loaded_tileset[selected_tile-1] = loaded_sprite
        
        #This is the start of the draw events.
        screen.fill((68, 36, 52))
        
        #Draw background for the sprite area.
        pygame.draw.rect(screen, color_black, (32, 32, 512, 512))
        
        #Draw the active sprite.
        if image_type != '':
            draw_position_x = 1
            draw_position_y = 1
            draw_color = color_black
            for character in loaded_sprite:
                draw_color = get_color(character)
                pygame.draw.rect(screen, draw_color, \
                                 (draw_position_x*32, \
                                  draw_position_y*32, 32, 32))
                draw_position_x += 1
                if draw_position_x > 16:
                    draw_position_x = 1
                    draw_position_y += 1
                
        #Draw the selected color under mouse if mouse is in sprite area.
        #Draw co-ordinates as well.
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x = math.floor(mouse_x/32)
        mouse_y = math.floor(mouse_y/32)
        if mouse_x >= 1 and mouse_x <= 16 and mouse_y >= 1 and mouse_y <= 16:
            pygame.draw.rect(screen, color_selected, \
                             (mouse_x*32, mouse_y*32, 32, 32))
            text_coordinates = font.render(str(mouse_x) + ',' + \
                                           str(mouse_y), False, color_white)
            text_coordinates_rect = text_coordinates.get_rect()
            text_coordinates_rect.center = (64, 16)
            screen.blit(text_coordinates, text_coordinates_rect)
            
        #Draw border around sprite area.
        pygame.draw.rect(screen, color_white, (32, 32, 512, 512), 1)
        
        #Draw the color pallette.
        pygame.draw.rect(screen, color_black, (576, 32, 32, 32))
        pygame.draw.rect(screen, color_purple, (608, 32, 32, 32))
        pygame.draw.rect(screen, color_dark_blue, (640, 32, 32, 32))
        pygame.draw.rect(screen, color_dark_gray, (672, 32, 32, 32))
        pygame.draw.rect(screen, color_brown, (576, 64, 32, 32))
        pygame.draw.rect(screen, color_dark_green, (608, 64, 32, 32))
        pygame.draw.rect(screen, color_red, (640, 64, 32, 32))
        pygame.draw.rect(screen, color_gray, (672, 64, 32, 32))
        pygame.draw.rect(screen, color_blue, (576, 96, 32, 32))
        pygame.draw.rect(screen, color_orange, (608, 96, 32, 32))
        pygame.draw.rect(screen, color_light_gray, (640, 96, 32, 32))
        pygame.draw.rect(screen, color_light_green, (672, 96, 32, 32))
        pygame.draw.rect(screen, color_peach, (576, 128, 32, 32))
        pygame.draw.rect(screen, color_light_blue, (608, 128, 32, 32))
        pygame.draw.rect(screen, color_yellow, (640, 128, 32, 32))
        pygame.draw.rect(screen, color_white, (672, 128, 32, 32))
        
        #Draw border around color palette.
        pygame.draw.rect(screen, color_white, (576, 32, 128, 128), 1)
        
        #Draw Transparent button.
        pygame.draw.rect(screen, color_transparent, (576, 160, 128, 32))
        pygame.draw.rect(screen, color_white, (576, 160, 128, 32), 1)
        screen.blit(text_transparent, text_transparent_rect)
        
        #Draw New Sprite button.
        pygame.draw.rect(screen, color_white, (576, 416, 128, 32), 1)
        screen.blit(text_new_sprite, text_new_sprite_rect)
        
        #Draw New Tileset button.
        pygame.draw.rect(screen, color_white, (576, 448, 128, 32), 1)
        screen.blit(text_new_tileset, text_new_tileset_rect)
        
        #Draw Save button.
        pygame.draw.rect(screen, color_white, (576, 480, 128, 32), 1)
        screen.blit(text_save, text_save_rect)
        
        #Draw Load button.
        pygame.draw.rect(screen, color_white, (576, 512, 128, 32), 1)
        screen.blit(text_load, text_load_rect)
        
        #Draw optional side panel if we are editing a sprite.
        if image_type == 'sprite':
            
            #Draw animate button with appropriate text based on value.
            pygame.draw.rect(screen, color_white, (18*32, 7*32, 128, 32), 1)
            if image_animated == 'true':
                screen.blit(text_animated, text_animated_rect)
            else:
                screen.blit(text_animated_not, text_animated_not_rect)
                
            #Draw frame button if sprite is animated.
            if image_animated == 'true':
                pygame.draw.rect(screen, color_white, (18*32, 8*32, 128, 32), 1)
                if image_frame == 1:
                    screen.blit(text_frame_one, text_frame_one_rect)
                else:
                    screen.blit(text_frame_two, text_frame_one_rect)
                    
            #Draw preview of sprite.
            draw_position_x = 1
            draw_position_y = 1
            draw_color = color_black
            for character in loaded_sprite:
                draw_color = get_color(character)
                pygame.draw.rect(screen, draw_color, \
                                 (draw_position_x*8 - 8 + 18*32, \
                                  draw_position_y*8 - 8 + 9*32, 8, 8))
                draw_position_x += 1
                if draw_position_x > 16:
                    draw_position_x = 1
                    draw_position_y += 1
                    
        #Draw optional side panel if we are editing a tileset.
        if image_type == 'tileset':
            tile_position_x = 1
            tile_position_y = 1
            for tile in loaded_tileset:
                draw_position_x = 1
                draw_position_y = 1
                draw_color = color_black
                for character in tile:
                    draw_color = get_color(character)
                    pygame.draw.rect(screen, draw_color, \
                                     (draw_position_x*2 - 2 + 18*32 + \
                                      tile_position_x*32 - 32, \
                                      draw_position_y*2 - 2 + 7*32 + \
                                      tile_position_y*32 - 32, 2, 2))
                    draw_position_x += 1
                    if draw_position_x > 16:
                        draw_position_x = 1
                        draw_position_y += 1
                tile_position_x += 1
                if tile_position_x > 4:
                    tile_position_x = 1
                    tile_position_y += 1
            #Draw grid around tiles.
            draw_color = color_white
            pygame.draw.rect(screen, draw_color, (18*32, 7*32, 128, 32), 1)
            pygame.draw.rect(screen, draw_color, (18*32, 8*32, 128, 32), 1)
            pygame.draw.rect(screen, draw_color, (18*32, 9*32, 128, 32), 1)
            pygame.draw.rect(screen, draw_color, (18*32, 10*32, 128, 32), 1)
            pygame.draw.rect(screen, draw_color, (18*32, 7*32, 32, 128), 1)
            pygame.draw.rect(screen, draw_color, (19*32, 7*32, 32, 128), 1)
            pygame.draw.rect(screen, draw_color, (20*32, 7*32, 32, 128), 1)
            pygame.draw.rect(screen, draw_color, (21*32, 7*32, 32, 128), 1)
        
        #Flip the display buffer to the screen.
        pygame.display.flip()
                
        clock.tick(30)
            
if __name__ == "__main__":
    main()
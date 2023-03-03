TILE_SIZE = 64
S_WIDTH = 1280
S_HEIGHT = 720 
FPS = 60

#ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
EXP_BAR_WIDTH = 200
ITEM_BOX_SIZE = 80
UI_FONT = 'assets/fonts/SuperMario256.ttf'
UI_FONT_SIZE = 18

HEALTH_COLOUR = 'red'
EXP_CLOUR = 'green'

#enemy
enemy_data = {
    'zombie' : {'health': 100, 'exp': 100, 'damage': 10, 'attach_type': 'zombie_swipe', 'attack_sound': 'none', 'speed': 1.5, 'knockback': 3, 'attack_radius': 5, 'notice_radius': 320}
}
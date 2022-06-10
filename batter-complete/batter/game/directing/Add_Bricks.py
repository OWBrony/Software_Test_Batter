import csv
from constants import *
from game.casting.animation import Animation
from game.casting.ball import Ball
from game.casting.body import Body
from game.casting.brick import Brick
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.racket import Racket
from game.casting.stats import Stats
from game.casting.text import Text 
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction
from game.scripting.collide_borders_action import CollideBordersAction
from game.scripting.collide_brick_action import CollideBrickAction
from game.scripting.collide_racket_action import CollideRacketAction
from game.scripting.control_racket_action import ControlRacketAction
from game.scripting.draw_ball_action import DrawBallAction
from game.scripting.draw_bricks_action import DrawBricksAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_racket_action import DrawRacketAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_ball_action import MoveBallAction
from game.scripting.move_racket_action import MoveRacketAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService
class BrickBoard():

    def __init__(self):
        pass

    def construct_bricks(self,cast):
        cast.clear_actors(BRICK_GROUP)
        
        stats = cast.get_first_actor(STATS_GROUP)
        level = stats.get_level() % BASE_LEVELS
        filename = LEVEL_FILE.format(level)

        with open(filename, 'r') as file:
            reader = csv.reader(file, skipinitialspace=True)
            for r, row in enumerate(reader):
                for c, column in enumerate(row):
                    x = FIELD_LEFT + c * BRICK_WIDTH
                    y = FIELD_TOP + r * BRICK_HEIGHT
                    color = column[0]
                    frames = int(column[1])
                    points = BRICK_POINTS 
                    
                    if frames == 1:
                        points *= 2
                    
                    position = Point(x, y)
                    size = Point(BRICK_WIDTH, BRICK_HEIGHT)
                    velocity = Point(0, 0)
                    images = BRICK_IMAGES[color][0:frames]

                    body = Body(position, size, velocity)
                    animation = Animation(images, BRICK_RATE, BRICK_DELAY)

                    brick = Brick(body, animation, points)
                    cast.add_actor(BRICK_GROUP, brick)
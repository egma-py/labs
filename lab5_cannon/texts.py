"""
here are all the necessary texts are shown in the game
"""
import pygame as pg

pg.font.init()

font = pg.font.Font(None, 25)
begin = font.render('New game', True, (0, 0, 0))
settings = font.render('Settings', True, (0, 0, 0))
exitt = font.render('Exit', True, (0, 0, 0))
returnn = font.render('Return', True, (0, 0, 0))
difficulty_txt = font.render('Difficulty', True, (0, 0, 0))
theme = font.render('Theme', True, (0, 0, 0))
location = font.render('Location', True, (0, 0, 0))
game_duration = font.render('Game time', True, (0, 0, 0)) 
sec10 = font.render('10 s', True, (0, 0, 0))
sec20 = font.render('20 s', True, (0, 0, 0))
sec30 = font.render('30 s', True, (0, 0, 0))
sec60 = font.render('60 s', True, (0, 0, 0))
hard = font.render('Hard', True, (0, 0, 0))
medium = font.render('Medium', True, (0, 0, 0))
easy = font.render('Easy', True, (0, 0, 0))
hills = font.render('Hills', True, (0, 0, 0))
plain = font.render('Plain', True, (0, 0, 0))
dark = font.render('Dark', True, (0, 0, 0))
light = font.render('Light', True, (0, 0, 0))
lost = font.render('YOU LOST', True, (0, 0, 0))
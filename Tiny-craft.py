from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import pyautogui
from perlin_noise import PerlinNoise
from numpy import floor
from scripts.house import * 
from scripts.tree import *
from datetime import time


game = Ursina()
grass_texture = load_texture('assets/grass.jpg')
stone_texture = load_texture('assets/stone.png')
brick_texture = load_texture('assets/brick.png')
dirt_texture = load_texture('assets/dirt.png')
wood_texture = load_texture('assets/wood_block.png')
glass_texture = load_texture('assets/glass1.png')
obsidan_texture = load_texture('Assets/obsidan.png')
ice_texture = load_texture('assets/ice.png')
sand_texture = load_texture('assets/sand.png')
white_stone_texture = load_texture('assets/white_stone.png')
sky_texture = load_texture('assets/skybox.png')
qoyish_sound = Audio('assets/menuin',loop = False, autoplay = False)
olish_sound = Audio('assets/menuout',loop = False, autoplay = False)

block_pick = 1

pyautogui.press("F11")
window.borderless = False
window.exit_button.enabled = False
window.fps_counter.enabled = False
window.cog_button.enabled = False
window.title = 'TINY-craft 1.3.0 version'



def update():
	global block_pick


	if held_keys['1']: block_pick = 1
	if held_keys['2']: block_pick = 2
	if held_keys['3']: block_pick = 3
	if held_keys['4']: block_pick = 4
	if held_keys['5']: block_pick = 5
	if held_keys['6']: block_pick = 6
	if held_keys['7']: block_pick = 7
	if held_keys['8']: block_pick = 8
	if held_keys['9']: block_pick = 9
	if held_keys['0']: block_pick = 10
	
	if held_keys['-']: 
		exit()




class Voxel(Button):
	def __init__(self, position = (0,0,0), texture = grass_texture):
		super().__init__(
			parent = scene,
			position = position,
			model = 'cube',
			origin_y = 0.5,
			texture = texture,
			color = color.color(0,0,random.uniform(0.85 ,1)))


	def input(self,key):
		if self.hovered:
			if key == 'left mouse down':
				qoyish_sound.play()
				if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
				if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
				if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
				if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
				if block_pick == 5: voxel = Voxel(position = self.position + mouse.normal, texture = wood_texture)
				if block_pick == 6: voxel = Voxel(position = self.position + mouse.normal, texture = glass_texture)
				if block_pick == 7: voxel = Voxel(position = self.position + mouse.normal, texture = obsidan_texture)
				if block_pick == 8: voxel = Voxel(position = self.position + mouse.normal, texture = ice_texture)
				if block_pick == 9: voxel = Voxel(position = self.position + mouse.normal, texture = sand_texture)
				if block_pick == 10: voxel = Voxel(position = self.position + mouse.normal, texture = white_stone_texture)








			if key == 'right mouse down':
				olish_sound.play()
				destroy(self)

noise = PerlinNoise(octaves=2, seed=300)
freq = 30
amp = 8

terrain_width = 60
for i in range(terrain_width*terrain_width):
	voxel = Voxel(position = (i))
	voxel.x = floor(i/terrain_width)
	voxel.z = floor(i%terrain_width)
	voxel.y = floor(noise([voxel.x/freq, voxel.z/freq]) * amp)
	

player = FirstPersonController(x=25,z=25,y=50)
Sky(texture='assets/sky.png')

night = time(7, 45, 1)


House(well_texture = 'Assets/brick', block_m = 'cube', model_glass = 'cube', glass_texture = 'Assets/glass1.png')


Tree(tree_texture = 'Assets/wood',
	leaf_texture = 'Assets/leaf', 
	model_tree = 'cube', 
	model_leaf = 'cube',
	onga = 30, 
	tepaga = 0.50, 
	togriga = 25)

Tree(tree_texture = 'Assets/birch_log',
	leaf_texture = 'Assets/leaf2', 
	model_tree = 'cube', 
	model_leaf = 'cube',
	onga = 9, 
	tepaga = 1.50, 
	togriga = 15)

Tree(tree_texture = 'Assets/wood',
	leaf_texture = 'Assets/leaf', 
	model_tree = 'cube', 
	model_leaf = 'cube',
	onga = 17, 
	tepaga = 0.50, 
	togriga = 26)

Tree(tree_texture = 'Assets/birch_log',
	leaf_texture = 'Assets/leaf2', 
	model_tree = 'cube', 
	model_leaf = 'cube',
	onga = 8, 
	tepaga = -2.50, 
	togriga = 5)

Tree(tree_texture = 'Assets/wood',
	leaf_texture = 'Assets/leaf', 
	model_tree = 'cube', 
	model_leaf = 'cube',
	onga = 52, 
	tepaga = 3.50, 
	togriga = 3)

Tree(tree_texture = 'Assets/wood',
	leaf_texture = 'Assets/leaf', 
	model_tree = 'cube', 
	model_leaf = 'cube',
	onga = 53, 
	tepaga = 0.50, 
	togriga = 22)

Tree(tree_texture = 'Assets/birch_log',
	leaf_texture = 'Assets/leaf2', 
	model_tree = 'cube', 
	model_leaf = 'cube',
	onga = 11, 
	tepaga = -0.50, 
	togriga = 39)

Tree(tree_texture = 'Assets/wood',
	leaf_texture = 'Assets/leaf', 
	model_tree = 'cube', 
	model_leaf = 'cube',
	onga = 34, 
	tepaga = 0.50, 
	togriga = 45)

Tree(tree_texture = 'Assets/birch_log',
	leaf_texture = 'Assets/leaf2', 
	model_tree = 'cube', 
	model_leaf = 'cube',
	onga = 46, 
	tepaga = -1.50, 
	togriga = 56)

 

game.run()
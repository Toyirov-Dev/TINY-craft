from ursina import *


if held_keys['0']:
	voxel = Voxel(position = self.position + mouse.normal, texture = 'wood')

def Tree(tree_texture = '', leaf_texture = '', model_tree = '', model_leaf = '', onga = '', tepaga = '', togriga = ''):


	# Daraxt poyasi
	block1 = Entity(model= model_tree,
		texture = tree_texture,
		collider= 'box',
		position=(onga, tepaga, togriga))

	b2 = tepaga + 1
	b3 = tepaga + 2
	b4 = tepaga + 3

	block2 = Entity(model= model_tree,
		texture = tree_texture,
		collider= 'box',
		position=(onga, b2, togriga))

	block3 = Entity(model= model_tree,
		texture = tree_texture,
		collider= 'box',
		position=(onga, b3, togriga))

	block4 = Entity(model= model_tree,
		texture = tree_texture,
		collider= 'box',
		position=(onga, b4, togriga))


	# Daraxt barglari
	ba1 = tepaga + 4

	barg1 = Entity(model= model_leaf,
		texture = leaf_texture,
		collider= 'box',
		position=(onga, ba1, togriga))

	onga2 = onga - 1
	tepa2 = tepaga + 3 

	barg2 = Entity(model= model_leaf,
		texture = leaf_texture,
		collider= 'box',
		position=(onga2, tepa2, togriga))

	onga3 = onga + 1
	
	barg3 = Entity(model = model_leaf,
		texture = leaf_texture,
		collider = 'box',
		position = (onga3, tepa2, togriga))

	turi = togriga + 1

	barg4 = Entity(model= model_leaf,
		texture = leaf_texture,
		collider= 'box',
		position=(onga2, tepa2, turi))

	turi2 = togriga - 1

	barg5 = Entity(model= model_leaf,
		texture = leaf_texture,
		collider= 'box',
		position=(onga2, tepa2, turi2))


	barg6 = Entity(model= model_leaf,
		texture = leaf_texture,
		collider= 'box',
		position=(onga3, tepa2, turi))


	barg7 = Entity(model= model_leaf,
		texture = leaf_texture,
		collider= 'box',
		position=(onga3, tepa2, turi2)) 

	barg8 = Entity(model= model_leaf,
		texture = leaf_texture,
		collider= 'box',
		position=(onga, tepa2, turi))


	barg9 = Entity(model= model_leaf,
		texture = leaf_texture,
		collider= 'box',
		position=(onga, tepa2, turi2)) 
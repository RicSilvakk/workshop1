import pyafai
from pyafai import objects
from pyafai import shapes
from random import randint

def main():
	world = pyafai.World2D()
	display =  pyafai.Display(world)


	obj = objects.pingPong(200,200)

	

	shape = shapes.Circle(10)
	obj.add_shape(shape)
	obj.angle = randint(10,360) 
	obj.velocity = 300#randint(50,350)
	 
	world.add_object(obj)

	pyafai.run()

if __name__ == '__main__':
	main()
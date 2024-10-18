import argparse
import maya.standalone
#Sets up the argparse arguments
parser = argparse.ArgumentParser()
parser.add_argument('-sh', '--shape', default=1, help="Choose a box or a sphere")
parser.add_argument('-s', '--size', default=1, help="Define the size of the cube")
parser.add_argument('-r', '--radius', default=1, help="Define the radius of the sphere")
args = parser.parse_args()

maya.standalone.initialize()
import maya.cmds as cmds
#makes the input by user an integer
shape=int(args.shape)
#determines based on user input whether to create a box or a sphere
if shape <= 1:
    cmds.polyCube(d=args.size, h=args.size, n='box01', w=args.size)
    print(f"Created a box of size {args.size}.")
else:
    cmds.polySphere(r=args.radius, n='sphere01')
    print(f"Created a sphere of size {args.radius}.")
#Creates and saves a file
maya.cmds.file(rename=r"D:\Users\Owner\Documents\Anim 435\anim-435-2024-ig345\assignment3\git\ig345_anim435_2024\assignment3\assignment3.mb")
maya.cmds.file(save=True)



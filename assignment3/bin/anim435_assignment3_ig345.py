import argparse
import maya.standalone

parser = argparse.ArgumentParser()
parser.add_argument('-sh', '--shape', default=1, help="Choose a box or a sphere")
parser.add_argument('-s', '--size', default=1, help="Define the size of the cube")
parser.add_argument('-r', '--radius', default=1, help="Define the radius of the sphere")
args = parser.parse_args()

maya.standalone.initialize()
import maya.cmds as cmds

shape=int(args.shape)
if shape <= 1:
    cmds.polyCube(d=args.size, h=args.size, n='box01', w=args.size)
    print(f"Created a box of size {args.size}.")
else:
    cmds.polySphere(r=args.radius, n='sphere01')
    print(f"Created a sphere of size {args.radius}.")

maya.cmds.file(rename=r"D:\Users\Owner\Documents\Anim 435\anim-435-2024-ig345\assignment3.mb")
maya.cmds.file(save=True)



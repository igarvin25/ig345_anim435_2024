import os
shot=os.getenv('SHOT')
numberOfPolys=int(os.getenv('POLYS'))


for n in range(numberOfPolys):
    maya.cmds.polyCube(n=shot)

poly = maya.cmds.ls(geometry=True)

for i in poly:
    lod = maya.cmds.addAttr(poly, sn="ran", ln="Random", min=1, max=5, dv=1, nn="Random")


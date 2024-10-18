#Create A Shape Without Opening Maya
## Overview
This python module allows you to create either a sphere or a cube with a size given by the user then saves the file.

## Usage

Note: Change the file path for the maya file in the python file before you start.

Open Git Bash
Type:
```
mayapy "FILEPATHOFPYTHONFILEHERE" -sh (1 or 2) -s (insert number) -r (insert number)
```

### Arguments
-sh or --shape : 1 = cube, 2 = sphere, defaults to 1
-s or --size : Any number you want which will become the height, width, and depth of the cube
-r or --radius : Any number you want which will become the radius of the cube

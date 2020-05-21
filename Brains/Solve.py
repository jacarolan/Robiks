import cv2
import numpy as np
from rubik_solver import utils

# 0-8 -> U
# 9-17 -> L
# 18-26 -> F
# 27-35 -> R
# 36-44 -> B
# 45-53 -> D
# Centers: U=4, L=13, F=22, R=31, B=40, D=49
# We need:  Y    B     R     G     O     W

U_center = 4
L_center = 13
F_center = 22
R_center = 31
B_center = 40
D_center = 49

Kociemba_U_center = 'y'
Kociemba_L_center = 'b'

Uonly = 'yyyyyyyyy' + 'ooobbbbbb' + 'bbbrrrrrr' + 'rrrgggggg' + 'gggoooooo' + 'wwwwwwwww' # This configuration of centers is necessary for kociemba
solve = utils.solve(Uonly, 'Kociemba')
print(solve)

UonlyRotated = 'yyyyyyyyy' + 'gggoooooo' + 'ooobbbbbb' + 'bbbrrrrrr' + 'rrrgggggg' + 'wwwwwwwww'
# solve = utils.solve(UonlyRotated, 'Kociemba')
# print(solve)

# Rotate a cube configuration about the vertical (Y) axis, keeping U and D faces fixed
def YRotate(cube):
	cubeArr = [c for c in cube]
	oldCubeArr = [c for c in cube]
	cubeArr[9:18], cubeArr[18:27], cubeArr[27:36], cubeArr[36:45] = oldCubeArr[36:45], oldCubeArr[9:18], oldCubeArr[18:27], oldCubeArr[27:36]
	image0to9 = [2, 5, 8, 1, 4, 7, 0, 3, 6]
	cubeArr[0:9] = [oldCubeArr[i] for i in image0to9]
	image45to53 = [51, 48, 45, 52, 49, 46, 53, 50, 47]
	cubeArr[45:53] = [oldCubeArr[i] for i in image45to53]
	return ''.join(cubeArr)

print(YRotate(YRotate(YRotate(UonlyRotated))))

# Rotate a cube configuration about the horizontal (X) axis, keeping L and R faces fixed
def XRotate(cube):
	cubeArr = [c for c in cube]
	oldCubeArr = [c for c in cube]
	cubeArr[36:45] = [oldCubeArr[i] for i in range(8, -1, -1)]
	cubeArr[0:9] = [oldCubeArr[i] for i in range(18, 27)]
	cubeArr[18:27] = [oldCubeArr[i] for i in range(45, 54)]
	cubeArr[45:54] = [oldCubeArr[i] for i in range(44, 34, -1)]
	image9to17 = [11, 14, 17, 10, 13, 16, 9, 12, 15]
	cubeArr[9:18] = [oldCubeArr[i] for i in image9to17]
	image27to35 = [33, 30, 27, 34, 31, 28, 35, 32, 29]
	cubeArr[27:36] = [oldCubeArr[i] for i in image27to35]
	return ''.join(cubeArr)

def orient(cube):
	if cube[U_center] == Kociemba_U_center:
		while cube[L_center] != Kociemba_L_center:
			cube = YRotate(cube)
		return cube
	elif cube[L_center] == Kociemba_L_center:
		while cube[U_center] != Kociemba_U_center:
			cube = XRotate(cube)
		return cube
	else:
		while not Kociemba_U_center in [cube[U_center], cube[F_center], cube[B_center], cube[D_center]]:
			cube = YRotate(cube)
		while Kociemba_U_center != cube[U_center]:

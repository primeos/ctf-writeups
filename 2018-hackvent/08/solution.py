#!/usr/bin/env nix-shell
#!nix-shell -I nixpkgs=/var/nixos-unstable -i python2 -p "python2.withPackages(ps: [ps.opencv])"

import cv2

im_gray = cv2.imread('code.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)

thresh = 127
im_binary = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]

binary_array = []
binary_matrix = []
for y in range(0, len(im_binary)):
    row = []
    for x in range(0, len(im_binary[y])):
        value = 0 if im_binary[y][x] != 0 else 1
        binary_array.append(value)
        row.append(value)
    binary_matrix.append(row)

def spiral_decode(inputMatrix):
    output = []

    max_x = len(inputMatrix)-1
    max_y = len(inputMatrix[0])-1
    assert max_x == max_y

    # Start at the center:
    pos_x = max_x/2
    pos_y = max_y/2
    assert pos_x == 12

    top_row = pos_y-1
    left_col = pos_x-1
    bottom_row = pos_y+1
    right_col = pos_x+1

    output.append(inputMatrix[pos_y][pos_x])

    edge_reached = False

    while top_row >= 0 or left_col >= 0 or bottom_row <= max_y or right_col <= max_x:

        # Up
        if top_row < 0:
            break
        for i in range(0, pos_y - top_row):
            pos_y -= 1
            output.append(inputMatrix[pos_y][pos_x])
        top_row -= 1
        if top_row == -1 and not edge_reached:
            edge_reached = True
            top_row = 0

        # Right
        if right_col > max_x:
            break
        for i in range(0, right_col - pos_x):
            pos_x += 1
            output.append(inputMatrix[pos_y][pos_x])
        right_col += 1
        if right_col == max_x+1 and not edge_reached:
            edge_reached = True
            right_col = max_x

        # Down
        if bottom_row > max_y:
            break
        for i in range(0, bottom_row - pos_y):
            pos_y += 1
            output.append(inputMatrix[pos_y][pos_x])
        bottom_row += 1
        if bottom_row == max_y+1 and not edge_reached:
            edge_reached = True
            bottom_row = max_y

        # Left
        if left_col < 0:
            break
        for i in range(0, pos_x - left_col):
            pos_x -= 1
            output.append(inputMatrix[pos_y][pos_x])
        left_col -= 1
        if left_col == -1 and not edge_reached:
            edge_reached = True
            left_col = 0

    return output

result = spiral_decode(binary_matrix)

print(''.join(str(val) for val in result))

solution = im_binary
for i in range(0, len(result)):
        value = 255 if result[i] == 0 else 0
        y = int(i/25)
        x = i%25
        solution[y][x] = value

cv2.imwrite('solution.png', solution)

print("Bits expected: " + str(25*25))
print("Bits read: " + str(len(result)))

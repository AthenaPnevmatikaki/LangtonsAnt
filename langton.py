import numpy as np
import cv2
import random


def show_map():
    img = cv2.resize(map, dim, interpolation=cv2.INTER_NEAREST)
    if inverted:
        color = (255, 255, 255)
    else:
        color = (0, 0, 0)
    img = cv2.putText(img, "Steps: " + str(counter), (img.shape[1] - 120, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color)
    cv2.imshow("Langton's Ant", img)
    return cv2.waitKey(delay)


number_of_ants = input("Enter number of ants: ")
if number_of_ants.isnumeric():
    number_of_ants = int(number_of_ants)
    if number_of_ants <= 0:
        print("Invalid number of ants, defaulting to 1")
        number_of_ants = 1
else:
    print("Invalid number of ants, defaulting to 1")
    number_of_ants = 1
delay = input("Enter delay between steps (ms) - minimum 1: ")
if delay.isnumeric():
    delay = int(delay)
    if delay <= 0:
        print("Invalid delay, defaulting to 1ms")
        delay = 1
else:
    print("Invalid delay, defaulting to 1ms")
    delay = 1
print("\nIf image window is behind console bring it forward!")

counter = 0
map_size = 250
x = []
y = []
facing = []
finished = []
inverted = False
orientations = ["up", "down", "right", "left"]
map = 255 * np.ones((map_size, map_size)).astype(np.uint8)
width = int(map.shape[1] * 4)
height = int(map.shape[0] * 4)
dim = (width, height)
show_map()
for i in range(0, number_of_ants):
    x.append(random.randint(2*map_size//5, 3*map_size//5))
    y.append(random.randint(2*map_size//5, 3*map_size//5))
    facing.append(orientations[random.randint(0, 3)])
    finished.append(False)
keep_running = True
while keep_running:
    for ant in range(0, number_of_ants):
        if finished[ant]:
            continue
        if map[y[ant], x[ant]] == 255:
            map[y[ant], x[ant]] = 0
            if facing[ant] == "up":
                facing[ant] = "right"
                if x[ant] < map_size-1:
                    x[ant] += 1
                else:
                    finished[ant] = True
                    continue
            elif facing[ant] == "right":
                facing[ant] = "down"
                if y[ant] < map_size-1:
                    y[ant] += 1
                else:
                    finished[ant] = True
                    continue
            elif facing[ant] == "down":
                facing[ant] = "left"
                if x[ant] > 0:
                    x[ant] -= 1
                else:
                    finished[ant] = True
                    continue
            elif facing[ant] == "left":
                facing[ant] = "up"
                if y[ant] > 0:
                    y[ant] -= 1
                else:
                    finished[ant] = True
                    continue
        elif map[y[ant], x[ant]] == 0:
            map[y[ant], x[ant]] = 255
            if facing[ant] == "up":
                facing[ant] = "left"
                if x[ant] > 0:
                    x[ant] -= 1
                else:
                    finished[ant] = True
                    continue
            elif facing[ant] == "right":
                facing[ant] = "up"
                if y[ant] > 0:
                    y[ant] -= 1
                else:
                    finished[ant] = True
                    continue
            elif facing[ant] == "down":
                facing[ant] = "right"
                if x[ant] < map_size-1:
                    x[ant] += 1
                else:
                    finished[ant] = True
                    continue
            elif facing[ant] == "left":
                facing[ant] = "down"
                if y[ant] < map_size-1:
                    y[ant] += 1
                else:
                    finished[ant] = True
                    continue
    keep_running = False
    for ant in range(0, number_of_ants):
        if not finished[ant]:
            keep_running = True
            break
    counter += 1
    key = show_map()
    if key == ord('i') or key == ord('I'):
        inverted = not inverted
        map = 255 - map
    elif key == ord('n') or key == ord('N'):
        xn = random.randint(5, map_size - 6)
        yn = random.randint(5, map_size - 6)
        map[yn-5:yn+5, xn-5:xn+5] = 255 * np.random.randint(0, 2, (10, 10)).astype(np.uint8)

cv2.waitKey(0)



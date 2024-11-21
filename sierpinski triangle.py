from math import sqrt
from gc import collect
from random import randint
from PIL import Image, ImageDraw
from loading_bar import LoadingBar


# CONSTANTS
FPS: int = 30
INTERVAL: int = 1
FRAME_COUNT: int = FPS * INTERVAL
DEPTH: int = 10
WHOLE_TRINAGLE: list[tuple[int, int]] = [(624, 0), (0, 1080), (1248, 1080)]
BACKGROUND_COLOR: tuple[int, int, int] = (0, 0, 0)
WINDOW_SIZE: tuple[int, int] = (1248, 1080)
RGB: list[tuple[int, int, int]] = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
INITIAL_SIDE: int = WHOLE_TRINAGLE[2][0] - WHOLE_TRINAGLE[1][0]
HALF_SIDE: float = INITIAL_SIDE / 2
HALF_HEIGHT: float =  INITIAL_SIDE * sqrt(3) / 2

# Variables
triangle = WHOLE_TRINAGLE
initial_points: list[tuple[int, int]] = [((triangle[0][0] + triangle[1][0]) // 2, (triangle[0][1] + triangle[1][1]) // 2),
                                         ((triangle[0][0] + triangle[2][0]) // 2, (triangle[0][1] + triangle[2][1]) // 2),
                                         ((triangle[1][0] + triangle[2][0]) // 2, (triangle[1][1] + triangle[2][1]) // 2)]

# Recursive drawing function
def sierpinski_triangle_recursive(depth_left: int, point: tuple[int, int]) -> None:
    # Recursion break condition
    if depth_left <= 0: return

    # Loop through corners
    for corner in triangle:
        new_point = (corner[0] + point[0]) // 2, (corner[1] + point[1]) // 2
        if new_point[0] >= 0 and new_point[1] <= WINDOW_SIZE[1]:
            draw.point(point, RGB[randint(0, 2)])
        sierpinski_triangle_recursive(depth_left - 1, new_point)

frames: list[Image.Image] = []
bar: LoadingBar = LoadingBar(FRAME_COUNT)
dpt = DEPTH
half_count: int = FRAME_COUNT // 2
for i in range(FRAME_COUNT):
    # increase of depth to compensate zoom
    if i == half_count:
        dpt += 1

    # Recalculate initial points
    lengthenning_side: int = int(HALF_SIDE * i / FRAME_COUNT)
    lengthenning_down: int = int(HALF_HEIGHT * i / FRAME_COUNT)
    triangle = [WHOLE_TRINAGLE[0],
                (WHOLE_TRINAGLE[1][0] - lengthenning_side, WHOLE_TRINAGLE[1][1] + lengthenning_down), 
                (WHOLE_TRINAGLE[2][0] + lengthenning_side, WHOLE_TRINAGLE[2][1] + lengthenning_down)]

    # Create an image with Pillow
    image = Image.new("RGB", WINDOW_SIZE, BACKGROUND_COLOR)
    draw = ImageDraw.Draw(image)
    for point, color in zip(triangle, RGB): draw.point(point, color)

    # Drawing triangle
    for halfway in triangle: sierpinski_triangle_recursive(dpt, halfway)

    frames.append(image)
    bar.update(i + 1)
    collect()

bar.close()

#frames[0].save("1.png")
#frames[-1].save("last.png")

# Saving image
frames[0].save(
    f"sierpinski_triangle_zoom.gif",
    save_all=True,
    append_images=frames[1:],
    optimize=True,
    duration=1000//FPS,
    loop=0
)


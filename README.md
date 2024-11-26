# Sierpiński Triangle Animation

This project generates an animated GIF of a Sierpiński triangle using Python's Pillow library. The script progressively zooms in on the triangle and animates its transformation, creating a visually appealing fractal effect.

## Description

The Sierpiński triangle is a well-known fractal consisting of equilateral triangles recursively subdivided into smaller triangles. This script allows you to visualize the recursive nature of the Sierpiński triangle by generating frames and saving them as an animated GIF.

The script divides the frame count into segments and gradually moves the triangle's vertices to create a zoom effect. The fractal depth (`DEPTH`) can be adjusted to add more or fewer recursive subdivisions.

### Key Features:
- Generates a Sierpiński triangle using recursive functions.
- Animates the zoom effect by progressively modifying the triangle's vertices.
- Uses Pillow to save the animation as an optimized GIF.

## Dependencies

- **Pillow**: A Python Imaging Library used to create and save images.
- **LoadingBar**: A utility to track the progress of the frame generation.

To install the required dependencies, run:
```bash
poetry install
```

## Usage

To generate the Sierpiński triangle animation, simply run the script. It will generate frames and save them as an animated GIF (`sierpinski_triangle_zoom.gif`) in the current directory.

The GIF will animate the zoom-in effect, and you can modify several parameters in the codeto customize the output:

- `FPS`: Frames per second of the GIF.
- `INTERVAL`: Length of the animation in seconds.
- `DEPTH`: Depth of recursion for the Sierpiński triangle.
- `WHOLE_TRIANGLE`: Initial points of the triangle.
- `BACKGROUND_COLOR`, `WINDOW_SIZE`, `RGB`: Customize the appearance of the triangle and window.

## Example

To run the script:
```bash
poetry run python sierpinski_triangle_pillow.py
```

The output will be saved as `sierpinski_triangle_zoom.gif`.

## Author
Wojciech Kośnik-Kowalczuk (<wojciech.kosnik.kowalczuk@gmail.com>)

## License
This project is licensed under the MIT License (see (LICENSE)[#LICENSE]).


# quaternionRubiks
Code for numerically representing a Rubik's Cube and the turning of its layers

This is just a simple repo containing some code for [a paper](https://github.com/kalyanoliveira/quaternionRubiks/files/9845835/quaternions.and.rubiks.cube.pdf) I wrote during high school. It explored the quaternion number system, and I tried to create a model where you could numerically represent a Rubik's cube, including the turning of its layers.

If you want to understand it, I'd say first read the paper. The next goal here is to used OpenCV to create an actual visualization of the cube.

On model.py, the creation of tables 1, 3, and 4 were implemented, alongside the actual process of rotating the cube. Currently, main.py just has some sample code showing the functioning of the algorithm.

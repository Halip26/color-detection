### What is Colour Detection?

Colour detection is the process of detecting the name of any color. Simple isn’t it? Well, for humans this is an extremely easy task but for computers, it is not straightforward. Human eyes and brains work together to translate light into color. Light receptors that are present in our eyes transmit the signal to the brain. Our brain then recognizes the color. Since childhood, we have mapped certain lights with their color names. We will be using the somewhat same strategy to detect color names.

### About the Python Project

In this color detection Python project, we are going to build an application through which you can automatically get the name of the color by clicking on them. So for this, we will have a data file that contains the color name and its values. Then we will calculate the distance from each color and find the shortest one.

### The Dataset

Colors are made up of 3 primary colors; red, green, and blue. In computers, we define each color value within a range of 0 to 255. So in how many ways we can define a color? The answer is 256*256*256 = 16,581,375. There are approximately 16.5 million different ways to represent a color. In our dataset, we need to map each color’s values with their corresponding names. But don’t worry, we don’t need to map all the values. We will be using a dataset that contains RGB values with their corresponding names. The CSV file for our dataset has been taken from this link:

[Color Dataset](https://github.com/codebrainz/color-names/blob/master/output/colors.csv)

The colors.csv file includes 865 color names along with their RGB and hex values.

### Prerequisites

Before starting with this Python project with source code, you should be familiar with the computer vision library of Python that is OpenCV and Pandas.

OpenCV, Pandas, numpy & argparse are the Python packages that are necessary for this project in Python. To install them, simply run this pip command in your terminal:

```
pip install opencv-python numpy pandas

pip install argparse

```

### How to run the script

- Provide your desired URL in the script or
- Input your image path on terminal to pick the colors plate from images
- Execute `python main.py -i "your image name"`

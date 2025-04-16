# utils.py
import os

def get_image_path(filename):
    """Returns the full path to an image in the images/ folder"""
    current_file = os.path.abspath(__file__)
    root_dir = os.path.dirname(current_file)  # Root of your project
    images_dir = os.path.join(root_dir, 'images')
    return os.path.join(images_dir, filename)

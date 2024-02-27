import cv2
import numpy as np

import math

def rotate_image(image, angle):
    # Get image dimensions
    height, width = image.shape[:2]

    # Calculate the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

    # Apply the rotation to the image
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

    return rotated_image

def line_angle(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    lines = cv2.HoughLines(edges, 1, np.pi/180, threshold=300)
    if isinstance(lines, np.ndarray):
        total_angle = 0
        for line in lines:
            rho, theta = line[0]
            total_angle += np.degrees(theta)

        # Find the average angle
        average_angle = total_angle / len(lines)

        return average_angle
    else:
        return 0

def auto_rotate(img):
    rot_angle = line_angle(img)
    rotated_image = rotate_image(img, rot_angle)
    return rotated_image

# Example usage
image_path = 'sample_image.jpeg'

# Read the image
img = cv2.imread(image_path)

rotated_image = auto_rotate(img)

# Original Image
cv2.imshow('Original Image', img)

# Rotated Image
cv2.imshow('Rotated Image', rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

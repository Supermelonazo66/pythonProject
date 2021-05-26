import cv2
from PIL import Image

class core:

    image = ""
    sensibility = 0

    def __init__(self, image, sensibility):
        self.image = cv2.imread(image)
        self.sensibility = sensibility

    def procesare(self):
        image = self.image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cv2.imwrite("temp.jpg", image)
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        _, binary = cv2.threshold(gray, self.sensibility, 255, cv2.THRESH_BINARY_INV)
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        image = cv2.drawContours(self.image, contours, -1, (0, 255, 0), 2)
        cv2.imwrite("temp.jpg", image)












import cv2
import numpy as np
import os
from datetime import datetime

class FaceDetector:
    def __init__(self):
        # Load the pre-trained face detection cascade classifier
        cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        
    def detect_faces(self, image):
        """Detect faces in the image and return their locations"""
        if isinstance(image, str):
            # If image is a file path, read it
            image = cv2.imread(image)
        
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        
        return faces
    
    def compare_faces(self, face1, face2, threshold=0.6):
        """Compare two face images and return True if they match"""
        # Resize images to same size
        size = (128, 128)
        face1 = cv2.resize(face1, size)
        face2 = cv2.resize(face2, size)
        
        # Convert to grayscale
        face1_gray = cv2.cvtColor(face1, cv2.COLOR_BGR2GRAY)
        face2_gray = cv2.cvtColor(face2, cv2.COLOR_BGR2GRAY)
        
        # Compare using structural similarity index
        score = cv2.matchTemplate(face1_gray, face2_gray, cv2.TM_CCOEFF_NORMED)[0][0]
        return score >= threshold
    
    def extract_face(self, image, face_location):
        """Extract face from image using location"""
        x, y, w, h = face_location
        return image[y:y+h, x:x+w]
    
    def save_face(self, image, face_location, save_path):
        """Save detected face to file"""
        face = self.extract_face(image, face_location)
        cv2.imwrite(save_path, face)
        return save_path

def init_face_detector():
    """Initialize the face detector"""
    return FaceDetector()

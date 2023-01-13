import cv2

class Detector:
    def __init__(self):
        self._faceDetection = cv2.CascadeClassifier('../Cascade/closed_frontal_palm.xml')
        self._image = None
        self._imageDetected = None
        self._statusDetection = False
        self._coordinates = {"xAxisInit": -1, "yAxisInit": -1, "xAxisEnd": -1, "yAxisEnd": -1, "width": -1, "height": -1}

    def detect(self, frame):
        self._image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self._faceDetection.detectMultiScale(
            grayImage, scaleFactor = 1.08, minNeighbors = 5, minSize = (85, 85), maxSize = (140, 140)
            )

        self._statusDetection = bool(len(faces))
        self._imageDetected = self._paint(faces) 
    
    def _paint(self, faces):
        for xAxis, yAxis, width, height in faces:
            cv2.rectangle(self._image, (xAxis, yAxis), (xAxis + width, yAxis + height), (0, 255, 255), 2)
            self._coordinates = {"xAxisInit": xAxis, "yAxisInit": yAxis, "xAxisEnd": xAxis + width, "yAxisEnd": yAxis + height, "width": width, "height": height}
        return self._image

    @property
    def coordinates(self):
        return self._coordinates

    @property
    def statusDetection(self):
        return self._statusDetection

    @property
    def imageDetected(self):
        return self._imageDetected
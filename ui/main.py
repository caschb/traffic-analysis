
import cv2
import tkinter.filedialog
import numpy as np

class SelectedRegion:
    def __init__(self):
        self.points = []
        self.filename = ""
        self.color = (124, 255, 50)
        self.thickness = 5

    def open_file(self):
        self.filename = tkinter.filedialog.askopenfilename(filetypes=[("Images",".jpg .png .jpeg")])
        self.img = cv2.imread(self.filename, 1)
        cv2.imshow('image', self.img)

    def add_point(self, event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN and len(self.points) < 4:
            self.points.append((x,y))
            cv2.circle(self.img, (x,y), self.thickness, self.color, -1)

    def print_points(self, state, optional):
        if len(self.points) == 4:
            points = np.array(self.points, np.int32)
            points = points.reshape((-1, 1, 2))
            cv2.polylines(self.img, [points], True, self.color, self.thickness)

    def run(self):
        cv2.setMouseCallback('image', self.add_point)
        cv2.createButton("Show region", self.print_points, cv2.QT_PUSH_BUTTON | cv2.QT_NEW_BUTTONBAR)
        while(1):
            cv2.imshow('image', self.img)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                cv2.destroyAllWindows()
                break


if __name__ == "__main__":
    region = SelectedRegion()
    region.open_file()
    region.run()



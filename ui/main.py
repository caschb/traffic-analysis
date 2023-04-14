
import cv2
import tkinter.filedialog

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        return x, y


if __name__ == "__main__":

    filename = tkinter.filedialog.askopenfilename(filetypes=[("Images",".jpg .png .jpeg")])
    img = cv2.imread(filename, 1)
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

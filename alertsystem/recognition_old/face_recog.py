import os
import sys
import cv2
import cv2.cv as cv
import numpy as np
import pickle

MODEL_FILE = "mug_model.mdl"
model_names={0:"Abhimanyu", 1:"Hemanth"}

def resize_img(img,nsize):
  nsize2 = (int(nsize*img.shape[1]/img.shape[0]),nsize)
  img2 = cv2.resize(src=img, dsize=nsize2, interpolation=cv.CV_INTER_AREA)
  return img2

def detect(img, cascade):
  gray = to_grayscale(img)
  rects = cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4, minSize=(3, 3), flags = cv2.CASCADE_SCALE_IMAGE)

  if len(rects) == 0:
    return []
  return rects

def detect_faces(img):
  cascade = cv2.CascadeClassifier("./Haarcascades/haarcascade_frontalface_alt.xml")
  return detect(img, cascade)

def to_grayscale(img):
  gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
  gray = cv2.equalizeHist(gray)
  return gray

def contains_face(img):
  return len(detect_faces(img)) > 0

def save(path, img):
  cv2.imwrite(path, img)

def crop_faces(img, faces):
  for face in faces:
    x, y, h, w = [result for result in face]
    return img[y:y+h,x:x+w]

def load_images_from_folder():
    images, labels = [],[]
    pickle_name = "mug.pck"
    c = open(pickle_name,'r')

    while True:
        try:
            img_labels = pickle.load(c)
        except:
            break

        label = img_labels[1]
        image_path = img_labels[0]
        print image_path
        try:
            cv_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            cv_image = cv2.resize(cv_image, (100,100))
            images.append(np.asarray(cv_image, dtype=np.uint8))
            labels.append(label)
        except IOError, (errno, strerror):
            print "IOError({0}): {1}".format(errno, strerror)

    return images, np.asarray(labels)


def train():
  images, labels = load_images_from_folder()
  #model = cv2.createFisherFaceRecognizer()
  model = cv2.createEigenFaceRecognizer()
  model.train(images,labels)
  model.save(MODEL_FILE)

def predict(cv_image):
  faces = detect_faces(cv_image)
  result = None
#  print len(faces)
  if len(faces) > 0:
    cropped = to_grayscale(crop_faces(cv_image, faces))
    resized = cv2.resize(cropped, (100,100))

    model = cv2.createFisherFaceRecognizer()
    #model = cv2.createEigenFaceRecognizer()
    model.load(MODEL_FILE)
    prediction = model.predict(resized)
    result = {
      'face': {
        'name': model_names[prediction[0]],
        'distance': prediction[1],
        'coords': {
          'x': str(faces[0][0]),
          'y': str(faces[0][1]),
          'width': str(faces[0][2]),
          'height': str(faces[0][3])
          }
       }
    }

  print "Found ", model_names[prediction[0]]

  return result


if __name__ == "__main__":
  # train()
  
  # print 'Training done. Next, predicting based on the given image.'
  
  cv_image = cv2.imread(sys.argv[1])
  try:
    cv_image = resize_img(cv_image, 200)
  except:
    print 'loading error'
  else:
    # cv2.imshow('Test subject',cv_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    predict(cv_image)
  

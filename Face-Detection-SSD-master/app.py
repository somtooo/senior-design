import crop_face as cf
import cfal as alf

# parameters for loading data and images
prototxt = 'ckpt_/deploy.prototxt.txt'
weights = 'ckpt_/res10_300x300_ssd_iter_140000.caffemodel'

# loading models
face_detection = alf.load_detection_model(prototxt, weights)

filename = "faceDetectionTest.mp4"

dirName = "/images"

# for detection and saved the crop the detected face 
a = cf.crop_face(filename, face_detection, dirName)

# for detection and align faces and saved the crop the detected face 
# a = afl.crop_face(filename, face_detection, dirName)

print("Done", a)


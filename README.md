# Face Recognition
## installation
pip install -r requirements.txt

## Movie

https://github.com/mehrnazsalehi/face_recognition/assets/149144017/4d35ae0b-829f-47e6-833a-803659539505

Developing a face recognition project using the OpenCV library and the Haar Cascade algorithm.
The most common way to detect a face (or any objects), is using the “Haar Cascade classifier”

Object Detection using Haar feature-based cascade classifiers is an effective object detection method proposed by Paul Viola and Michael Jones in their paper, “Rapid Object Detection using a Boosted Cascade of Simple Features” in 2001. It is a machine learning-based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images.

Here we will work with face detection. Initially, the algorithm needs a lot of positive images (images of faces) and negative images (images without faces) to train the classifier. Then we need to extract features from it. The good news is that OpenCV comes with a trainer as well as a detector. If you want to train your own classifier for any object like car, planes etc. you can use OpenCV to create one. Its full details are given here: Cascade Classifier Training.

If you do not want to create your classifier, OpenCV already contains many pre-trained classifiers for face, eyes, smile, etc. Those XML files can be downloaded from the Harcade directory.

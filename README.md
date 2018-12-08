# YOHO

YOHO(Yoo and Horne) Mouth movement detector.

## How to run video decomposer

```
python3 decompose_video.py -f <path to video file> -d <directory to save frames in>
```

## How to run mouth detector

```
python3 facial_landmarks.py -p <path to shape_predictor_68_face_landmarks.dat> -d <directory where images are stored>
```

## How to run cropping tool

```
python3 crop.py -d <directory where images to crop are stored>
```

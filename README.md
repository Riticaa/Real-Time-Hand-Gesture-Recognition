# 🖐️ Real-Time Hand Gesture Recognition System

---

## 📌 Overview

This project is a **real-time hand gesture recognition system** built using Computer Vision techniques. It detects hand gestures using a webcam and prints the recognized gesture directly in the **terminal (CLI)** without any graphical interface.

The system leverages **MediaPipe for hand landmark detection** and custom logic to classify gestures such as:

* ✋ Open Palm
* ✊ Fist
* 👍 Thumbs Up
* ✌️ Peace

---

## 🎯 Problem Statement

Traditional input methods like keyboards and touchscreens are not always convenient or accessible. There is a need for a **touchless, real-time interaction system** that can interpret human gestures effectively.

This project aims to provide a **simple, low-cost gesture recognition system** that works in real time and can be extended to control applications or assist accessibility.

---

## 🚀 Features

* Real-time hand detection using webcam
* Recognition of multiple gestures
* CLI-based output (no GUI required)
* Lightweight and fast execution
* Easy to extend with new gestures

---

## 🛠️ Tech Stack

* Python
* OpenCV
* MediaPipe
* NumPy

---

## 📂 Project Structure

```
gesture-recognition-cli/
│
├── main.py                # Entry point of the application
├── gesture_logic.py      # Core gesture detection logic
├── utils/
│   └── landmarks.py      # Helper functions for landmark processing (optional)
│
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

## 🧩 Structure Explanation

### 🔹 `main.py`

* Handles webcam input using OpenCV
* Processes frames in real-time
* Uses MediaPipe to extract hand landmarks
* Calls gesture detection logic
* Prints detected gestures in CLI

---

### 🔹 `gesture_logic.py`

* Contains the core logic for gesture recognition
* Uses landmark positions to determine finger states
* Implements rule-based classification for gestures

Example:

* Fingers open → Open Palm
* Fingers closed → Fist
* Thumb up → Thumbs Up

---

### 🔹 `utils/landmarks.py` (Optional)

* Utility functions for processing landmarks
* Improves code modularity and readability

---

### 🔹 `requirements.txt`

* Lists all required Python libraries
* Used to set up the environment quickly

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/gesture-recognition-cli.git
cd gesture-recognition-cli
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Run the Project

```
python main.py
```

---

## 💻 CLI Output Example

```
Gesture Detected: OPEN PALM ✋
Gesture Detected: FIST ✊
Gesture Detected: THUMBS UP 👍
Gesture Detected: PEACE ✌️
```

---

## 📊 Working Principle

1. Webcam captures video frames
2. MediaPipe detects 21 hand landmarks
3. Landmark positions are analyzed
4. Finger states are determined (open/closed)
5. Gesture is classified using rule-based logic
6. Output is displayed in terminal

---

## 🔥 Future Improvements

* Add more gesture classes
* Integrate voice feedback
* Control system applications using gestures
* Train a machine learning model for better accuracy
* Add multi-hand detection

---

## ⚠️ Challenges Faced

* Handling different lighting conditions
* Maintaining real-time performance
* Accurate gesture classification using rule-based logic

---

## 📌 Conclusion

This project demonstrates the practical application of **Computer Vision in real-time systems**. It provides a simple yet effective solution for gesture-based interaction and serves as a foundation for more advanced AI-based systems.

---

## 👩‍💻 Author

* Ritica Awasthi

---

## 📜 License

This project is for educational purposes.

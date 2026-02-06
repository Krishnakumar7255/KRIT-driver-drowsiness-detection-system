# KRIT-driver-drowsiness-detection-system
Road safety is one of the most critical challenges in modern transportation. Driver fatigue and drowsiness are among the leading causes of accidents worldwide. The KRIT Driver Drowsiness Detection System is a machine learning–based solution designed to monitor driver alertness in real time and provide timely warnings to prevent mishaps.
This project combines computer vision, facial landmark detection, and ML algorithms to identify signs of drowsiness such as prolonged eye closure, frequent blinking, yawning, and head tilts.

✨ Features
- Real-Time Monitoring: Continuous tracking of driver’s face using a camera.
- Eye & Blink Detection: Measures blink frequency and eye closure duration.
- Yawn Detection: Identifies mouth opening patterns linked to fatigue.
- Head Pose Estimation: Detects nodding or head tilts.
- Alert System: Audio/visual alarms when drowsiness is detected.
- Lightweight Implementation: Runs efficiently on laptops, Raspberry Pi, or in-vehicle systems.
- Scalable Design: Can be integrated into cars, simulators, or fleet management systems.

🛠 Tech Stack
- Programming Language: Python
- Libraries:
- OpenCV (image processing & video capture)
- dlib (facial landmark detection)
- NumPy (numerical computations)
- TensorFlow/Keras (optional ML models for advanced detection)
- Hardware: Standard webcam or in-vehicle camera

⚙️ How It Works
- Face Detection → Capture driver’s face using OpenCV.
- Landmark Extraction → Use dlib to detect eyes, mouth, and head position.
- Feature Analysis → Calculate blink rate, eye closure duration, yawning frequency.
- Classification → Apply ML/threshold-based logic to determine drowsiness.
- Alert Trigger → If drowsiness detected, system issues audio/visual warning.

🚀 Installation & Usage
# Clone the repository
git clone https://github.com/yourusername/KRIT-Drowsiness-Detection.git

# Navigate to project folder
cd KRIT-Drowsiness-Detection

# Install dependencies
pip install -r requirements.txt

# Run the system
python drowsiness_detection.py



📂 Project Structure
KRIT-Drowsiness-Detection/
│── src/                 # Source code
│   ├── drowsiness_detection.py
│   ├── utils.py
│── requirements.txt     # Dependencies
│── README.md            # Documentation



🎯 Use Cases
- Personal vehicles for enhanced road safety.
- Commercial fleets to reduce accidents and insurance costs.
- Driving schools and simulators for training purposes.
- Research projects in computer vision and AI safety systems.

🔮 Future Improvements
- Integration with IoT for fleet-wide monitoring.
- Cloud-based analytics dashboard.
- Advanced deep learning models for higher accuracy.
- Multi-driver support in shared vehicles.

🤝 Contributing
Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request.

📜 License
This project is licensed under the MIT License.

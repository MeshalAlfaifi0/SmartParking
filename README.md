# Smart Parking System

An integrated smart parking management system using artificial intelligence aims to improve the driver experience and increase the efficiency of parking operations by monitoring parking spaces in real-time and automatically directing vehicles to available spaces using smart traffic lights and an electronic information panel.

# Project Idea

The system helps drivers find parking spaces quickly and effortlessly, reducing congestion within parking spaces by analyzing parking conditions in real-time and directing vehicles based on the nearest available space.

The system also identifies unlicensed or suspicious vehicles and sends direct alerts to security authorities.

It also provides a smart information panel that enables drivers to accurately locate their vehicle upon returning.

## Technologies Used

- YOLO (for vehicle detection and parking status recognition)
- OpenCV (for image and video processing)
- FastAPI (for developing a software interface that connects systems)
- Arduino (for controlling traffic lights and parking guidance)
- Wokwi (for virtual simulation and testing of the system)
- Roboflow (for preparing training data and improving model performance)

## System Features

- Real-time and accurate guidance for drivers to available parking spaces via traffic lights.
- Improved safety by detecting unknown vehicles and sending instant alerts.
- An electronic information panel shows the driver's vehicle location upon return.
- A dashboard displays live data to help management make better decisions.
- The system can be expanded to include parking spaces at major facilities such as universities, hospitals, and airports.

## Project Files

- `data.yaml`: Information about the training categories and data environment.
- `yolo_model/`: Files for the model trained to detect parking spaces.
- `arduino/parking_system.ino`: Arduino code for controlling traffic lights.
- `images/`: Images illustrating the results of the model or system.
- `README.dataset.txt`: Explanation of the data preparation used for training.
- `README.roboflow.txt`: Details on preparing the data using Roboflow.
- `wokwi_link.txt`: Link to the system simulation on Wokwi.

## Project Objectives

- Reduce parking search time by up to 50%.
- Significantly reduce parking congestion.
- Increase security by tracking suspicious vehicles.
- Improve the user experience in parking lots from entry to rapid parking.
- Enable management to monitor and analyze data to make better operational decisions.
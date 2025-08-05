<!--
Hey, thanks for using the awesome-readme-template template.  
If you have any enhancements, then fork this project and create a pull request 
or just open an issue with the label "enhancement".

Don't forget to give this project a star for additional support ;)
Maybe you can mention me or this repo in the acknowledgements too
-->
<div align="center">

![Logo](assets/Hardware_Image_1.png)

# Automatic Medication Dispenser In Order To Reduce Medication Non-Adherence  

This project is an AI-powered automatic medication dispenser designed to improve medication adherence using a combination of image recognition, OCR, and natural language processing. The system is built for patients, caregivers, and healthcare providers to ensure safe and timely medication intake — all while being monitored remotely through a mobile app.

It integrates hardware control (Arduino), YOLO-based pill recognition, and a custom-trained spaCy NLP model to extract dosage and frequency instructions from prescription labels. A PyQt6 desktop interface manages the system on-device, and a mobile app enables remote supervision. 

All the resources I used for this project can be found in the following Google Drive, linked for your reference: https://drive.google.com/drive/folders/1BSqckdxfqDh0ZibXCd9fYPzXVN9h-TSW 

[![Contributors](https://img.shields.io/github/contributors/SophieBarriault/Dispenser)](https://github.com/SophieBarriault/Dispenser/graphs/contributors)
[![Last Commit](https://img.shields.io/github/last-commit/SophieBarriault/Dispenser)](https://github.com/SophieBarriault/BioPredict-Regression-Models-for-Synthetic-Biology)
[![Forks](https://img.shields.io/github/forks/SophieBarriault/BioPredict-Regression-Models-for-Synthetic-Biology)](https://github.com/SophieBarriault/BioPredict-Regression-Models-for-Synthetic-Biology/network/members)
[![Stars](https://img.shields.io/github/stars/SophieBarriault/BioPredict-Regression-Models-for-Synthetic-Biology)](https://github.com/SophieBarriault/BioPredict-Regression-Models-for-Synthetic-Biology/stargazers)
[![Issues](https://img.shields.io/github/issues/SophieBarriault/BioPredict-Regression-Models-for-Synthetic-Biology)](https://github.com/SophieBarriault/BioPredict-Regression-Models-for-Synthetic-Biology/issues)
[![License](https://img.shields.io/github/license/SophieBarriault/BioPredict-Regression-Models-for-Synthetic-Biology.svg)](https://github.com/SophieBarriault/BioPredict-Regression-Models-for-Synthetic-Biology/blob/main/LICENSE)

[View Demo](https://github.com/sophiebarriault/BioPredict) ·
[Documentation](https://github.com/sophiebarriault/BioPredict) ·
[Report Bug](https://github.com/sophiebarriault/BioPredict/issues) ·
[Request Feature](https://github.com/sophiebarriault/BioPredict/issues)

</div>

---

# 📔 Table of Contents

- [About the Project](#-about-the-project)
  - [Screenshots](#-screenshots)
  - [Tech Stack](#-tech-stack)
  - [Features](#-features)
  - [Color Reference](#-color-reference)
  - [Environment Variables](#-environment-variables)
- [Getting Started](#-getting-started)
  - [Prerequisites](#-prerequisites) 
  - [Run Locally](#-run-locally)
  - [Deployment](#-deployment) 
- [FAQ](#-faq)
- [License](#-license)
- [Contact](#-contact)
- [Acknowledgements](#-acknowledgements-) 


---

## 🌟 About the Project

This project presents an AI-powered automatic medication dispenser designed to improve medication adherence and safety for patients. Initially developed for the Massachusetts Science & Engineering Fair (MSEF), the device advanced to the State Level Finalist round, where it was recognized for its innovative integration of machine learning, computer vision, and IoT technologies in a healthcare setting. 


**Goal:**

To create an accessible, intelligent system that ensures patients take the correct medications at the correct times — reducing errors, improving adherence, and offering peace of mind for caregivers and family members. 



**Core Features:**

 - Image recognition model to verify whether medication has been taken correctly.

 - OCR + NLP (Named Entity Recognition) to extract dosage instructions from prescription labels.

 - Arduino-controlled dispensing system triggered by AI verification and scheduled reminders.

 - Mobile + Desktop interface (via Toga framework) for caregiver monitoring and remote updates.

 - Video evidence recording for accountability and patient monitoring. 



**Recognition:**  

 - Filed for a provisional patent for the design and idea December 2024 

 - Selected for the Massachusetts Science & Engineering Fair (MSEF) Regional Round

 - Advanced to the MSEF State Level Competition as a Finalist

 - Praised for its real-world impact, interdisciplinary approach, and scalable potential



---

### 📷 Demo Video 

Click to watch the demo here! 

[![Watch the Demo Video](assets/to_demo.png)](https://drive.google.com/file/d/1wByr87FT2HsipwZgwH-gzBg_70QS4TUb/view?usp=sharing) 


---

### 👾 Tech Stack

- **Python** – Core programming language for the application

- **Toga** – GUI framework for building cross-platform desktop and mobile apps 
- **Buildozer** - GUI framework for both Android and IOS compatibility 

- **OpenCV** – Real-time image processing and integration with camera for pill verification

- **Tesseract OCR** – Optical Character Recognition for extracting text from prescriptions

- **spaCy** – Custom Named Entity Recognition (NER) model to extract dosage/frequency info

- **YOLOv8** – Object detection model to monitor pill intake and hand movement

- **Flask** – Lightweight server to handle requests between the app and ML models

- **PySerial** – Communication between the Python app and the Arduino board

- **Arduino** – Controls pill dispensing mechanism (via servo motors, etc.)

- **Git & GitHub** – Version control and project collaboration

---

### 🎯 Features

- **Automated Pill Dispensing** 
  Dispenses the correct medication at the right time using an Arduino-controlled mechanism, reducing the risk of missed or incorrect doses.

- **Real-Time Pill Intake Monitoring** 
  Utilizes a YOLOv5-based image recognition system to track the sequence: pill present → pill taken → hand empty — confirming successful medication intake.

- **Custom OCR Processing** 
  Uses Tesseract OCR to extract medication names, dosages, and instructions from images of prescriptions or labels.

- **Medical NER Model** 
  A custom-trained spaCy Named Entity Recognition (NER) model processes OCR output to identify key medical information like dosage frequency and medication schedules.

- **Cross-Platform Interface (Toga + Buildozer)** 
  Built using the Toga framework for both desktop and mobile (Android and IOS) platforms, allowing caregivers and users to interact with the system easily.

- **Flask-Based Communication** 
  A lightweight Flask server connects the app to backend ML models, ensuring fast and reliable processing of user input and image recognition results.

- **Emergency Alert System** 
  If a user fails to take their medication within a set time frame, the system plays an audio alert and notifies a connected caregiver.

- **Time-Based Triggers** 
  The application runs on a schedule, automatically activating the camera and dispenser based on predefined medication times.

- **PDF Report Generation** 
  Extracted text from prescriptions is automatically saved and compiled into a downloadable PDF for easy recordkeeping and sharing with healthcare providers.


---

### 🎨 Color Reference

| Color             | Hex        |
| ----------------- | ---------- |
| Primary Color     | `#0074d9`  |
| Secondary Color   | `#00e0ff`  |
| Accent Color      | `#ffffff`  |
| Text Color        | `#00e0ff`  |

---

### 🔑 Environment Variables

To run this project, add the following to your `.env` file:



<!-- Getting Started -->
## 	:toolbox: Getting Started

<!-- Prerequisites -->
### :bangbang: Prerequisites

This project uses NumPy, Pandas, Matplotlib, and Sklearn 

```bash
 pip install numpy 
 pip install pandas
 pip install matplotlib
 pip install scikit-learn 
```
<!-- Run Locally -->
### :running: Run Locally

Clone the project

```bash
  git clone https://github.com/SophieBarriault/BioPredict-Regression-Models-for-Synthetic-Biology.git
```

Go to the project directory

```bash
  cd BioPredict-Regression-Models-for-Synthetic-Biology 
```

Install dependencies

```bash 
  cd Dispenser 
  pip install -r requirements.txt 
```

<!-- Deployment -->
### :triangular_flag_on_post: Deployment

To deploy the mobile application simulation software, run: 

```bash 
  cd Dispenser/App/andriod_app
  python app.py 
```

To deploy the medication dispenser software, run: 

```bash 
  cd Dispenser/App
  python App_For_Monitering.py 
``` 




 
<!-- Contact -->
## :handshake: Contact

Sophie Barriault - [Linkedin](www.linkedin.com/in/sophie-barriault) - sophiebarriaultofficial@gmail.com 

Project Link: [https://github.com/Louis3797/awesome-readme-template](https://github.com/Louis3797/awesome-readme-template)


<!-- Acknowledgments -->
## :gem: Acknowledgements 

Useful resources and libraries that I've used in my project: 


 - [Scikit-learn](https://scikit-learn.org/stable/) 
 - [Pandas](https://pandas.pydata.org/) 
 - [NumPy](https://numpy.org/) 
 - [Matplotlib](https://matplotlib.org/) 
 - [Logisitc Regression ML Models Overview](https://www.geeksforgeeks.org/machine-learning/understanding-logistic-regression/)
 - [Linear Regression ML Models Overview](https://www.geeksforgeeks.org/machine-learning/ml-linear-regression/) 
 - [Shields.io](https://shields.io/)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [Emoji Cheat Sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md#travel--places)
 - [Readme Template](https://github.com/othneildrew/Best-README-Template) 






















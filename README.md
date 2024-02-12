# FocusMate: Smart Pomodoro Clock with Face Recognition and Productivity Enhancements

![Project Image](https://wethegeek.com/wp-content/uploads/2019/10/pomodoro-technique.png)

## Table of Contents

- [Description](#description)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Description

Pomodoro Face Recognition is a specialized Pomodoro clock that enhances productivity and well-being. It combines the Pomodoro technique with face recognition using OpenCV to create a unique work environment. Key features include:

- **Face Presence Detection:** The clock actively monitors if the user is present in front of the camera during work sessions. If the user is not detected, an alarm is triggered to encourage presence.

- **Pomodoro Timer:** The clock follows the traditional Pomodoro technique with customizable working and interval times. Upon completing a Pomodoro session, a notification tone prompts the user to take a break.

- **Presence Validation:** If the user fails to leave their working place within the allotted break time, a persistent alarm is activated until the user leaves. This ensures a healthy break and prevents overworking.

- **Interval Notifications:** After the break, the clock notifies the user when the interval is finished, prompting them to return and resume work.

- **Sleepiness Detection:** The system detects signs of sleepiness and activates an alarm to alert the user, encouraging them to stay focused and engaged.

## Project History

This project, developed in 2021, serves as a personal initiative to enhance productivity using a unique approach to the Pomodoro technique. 

## Prerequisites

- Python 3.7
- OpenCV
- imutils
- numpy
- pygame

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/tharindusathsarahome/FocusMate.git
    cd FocusMate
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Download the pre-trained model and audio files and place them in the `data` directory.

## Usage

To run the Pomodoro Face Recognition clock, use the following command:

```bash
python main.py
```

Specify the `-w` or `--window` flag to display the camera window:

```bash
python main.py -w True
```

## Configuration

Adjust the Pomodoro and Interval times in the script according to your preferences:

```python
PomodoroTime = 1500  # 25 minutes in seconds
IntervalTime = 300   # 5 minutes in seconds
```
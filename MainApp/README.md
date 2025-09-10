# Eye Relief: Smart Screen Break Assistant

![Eye Relief Logo](https://img.shields.io/badge/Eye%20Relief-Vision%20Protection-blue)
![Python](https://img.shields.io/badge/Python-3.x-green)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-orange)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.x-purple)

Eye Relief is a computer vision application designed to help prevent digital eye strain by monitoring screen time and enforcing healthy viewing habits.

## Features

- **Automatic Face Detection**: Uses your webcam to detect when you're looking at the screen
- **Timed Breaks**: Alerts you after 10 minutes of continuous screen time
- **Break Enforcement**: Verifies you've actually looked away from the screen
- **Voice Notifications**: Provides audio prompts without requiring you to read more text
- **Real-time Monitoring**: Continuously checks if you're following the recommended break patterns

## Why Eye Relief?

Digital eye strain affects millions of people who spend extended periods in front of screens. This application helps implement the 20-20-20 rule recommended by eye care professionals:
- Every 20 minutes
- Look at something 20 feet away
- For at least 20 seconds

## Tech Stack

- **Python 3.x**: Core programming language
- **OpenCV**: Camera capture and image processing
- **MediaPipe**: Facial landmark detection for precise tracking
- **pyttsx3**: Text-to-speech voice notifications
- **Time module**: Session timing management

## Installation

1. Clone this repository or download the source code:
```
git clone https://github.com/yourusername/eye-relief.git
```

2. Navigate to the project directory:
```
cd eye-relief
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

4. Ensure your webcam is connected and working properly

## Usage

1. Run the application:
```
python eye_reliefbeta.py
```

2. Position yourself in front of your webcam so your face is visible
3. Continue your work normally
4. When prompted to take a break, look away from your screen at a distant object
5. Return to your work once the application confirms you've taken an adequate break

## Requirements

See the `requirements.txt` file for a complete list of dependencies.

## Future Enhancements

- Customizable break intervals
- Eye blink rate detection
- Statistics tracking for daily screen time
- Adjustable sensitivity settings
- Dark mode / light mode UI
- Minimize to system tray option

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the OpenCV and MediaPipe teams for their incredible computer vision libraries
- Inspired by the 20-20-20 rule recommended by optometrists

---

*Take care of your eyes, they're the only pair you've got!*

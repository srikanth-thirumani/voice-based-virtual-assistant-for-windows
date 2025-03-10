# 🔊 Windows Voice Assistant

<div align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/platform-Windows-lightgrey.svg" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</div>

## 🌟 Overview

Windows Voice Assistant is an advanced voice-controlled personal assistant designed for Windows, capable of performing various tasks through natural language commands. It uses speech recognition and text-to-speech technologies to create a hands-free computing experience.

## ✨ Features

- 🎤 Wake word detection ("Hi Windows", "Hello Windows", "Hey Windows")
- 🗣️ Natural language command processing
- 🌐 Web browsing and searches (Google, YouTube, LinkedIn)
- 📊 System information monitoring
- 📧 Email composition and sending
- 📱 WhatsApp messaging
- 🎵 YouTube music playback
- 📷 Camera control and screenshots
- 🌦️ Weather information
- 📰 News updates
- 🎮 System control (shutdown)
- 🖼️ AI image generation using Stability AI
- 🤖 AI responses using Google's Gemini for unrecognized commands
- 📝 Note-taking functionality
- 🌍 Navigation and directions
- 🔍 IP address checking
- 🚀 Internet speed testing

## 🛠️ Technologies Used

- **Python** - Core programming language
- **pyttsx3** - Text-to-speech conversion
- **SpeechRecognition** - Voice command recognition
- **OpenCV** - Camera functionality
- **PIL** - Image processing
- **Stability SDK** - AI image generation
- **Google Gemini AI** - AI conversation fallback
- **PyWhatKit** - WhatsApp messaging and YouTube playback
- **PyAutoGUI** - Screenshot functionality
- **Speedtest** - Internet speed testing
- **Requests** - API interactions for weather, news, etc.

## 🚀 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/srikanth-thirumani/windows-voice-assistant.git
   cd windows-voice-assistant
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with your API keys:
   ```
   DREAMSTUDIO_API=your_stability_ai_api_key
   ```

## 📋 Required API Keys

- **Stability AI API** - For image generation
- **Google Gemini API** - For AI responses
- **OpenWeatherMap API** - For weather information
- **News API** - For news updates
- **OMDb API** - For movie information

## 🎮 Usage

1. Run the assistant:
   ```bash
   python voice_assistant.py
   ```

2. Activate with wake word:
   - Say "Hi Windows", "Hello Windows", or "Hey Windows"

3. After hearing "Yes, how can I assist you?", speak your command.

## 📝 Command Examples

- "Open Chrome"
- "Search for Python tutorials on Google"
- "What time is it?"
- "Check the weather in New York"
- "Send a WhatsApp message"
- "Take a screenshot"
- "Generate an image of a mountain landscape"
- "Check my internet speed"
- "Tell me a joke"
- "Play music on YouTube"
- "What's my IP address?"
- "System information"
- "Latest news"

## 🔄 Command Keywords

The assistant recognizes various command keywords for each function:

```
'shutdown': ['shutdown', 'power down', 'turn off']
'open chrome': ['chrome', 'google chrome', 'open chrome']
'send whatsapp message': ['send whatsapp message', 'whatsapp', 'message on whatsapp']
'generate image': ['generate image', 'create image', 'create a picture', 'make picture']
```

## 🧩 Project Structure

```
windows-voice-assistant/
│
├── voice_assistant.py - Main application file
├── .env - Environment variables and API keys
├── requirements.txt - Required Python packages
└── README.md - Project documentation
```

## 🔧 Customization

You can customize the assistant by:

1. Adding new command keywords to the `command_keywords` dictionary
2. Implementing new functions for additional features
3. Modifying existing functions to change behavior

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Thirumani Srikanth**

- GitHub: [srikanth-thirumani](https://github.com/srikanth-thirumani)
- LinkedIn: [Srikanth Thirumani](https://www.linkedin.com/in/srikanth-thirumani-136180281)
- Email: srikanththirumani01@gmail.com

## 🙏 Acknowledgements

- **Python Speech Recognition** community
- **Stability AI** for image generation capabilities
- **Google** for Gemini AI integration
- **OpenWeatherMap** for weather data
- **News API** for news content

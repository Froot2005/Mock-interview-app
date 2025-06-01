# Mock-interview-app
# AI-Powered Interview Application

A sophisticated interview application that conducts automated voice interviews using Vapi.ai and Twilio integration. The application provides real-time transcription, natural conversation flow, and intelligent interview management.

## Features

- 🎙️ Real-time voice interviews with AI
- 📝 Live transcription using Deepgram
- 🤖 Natural language processing for dynamic conversations
- 📱 Phone call integration via Twilio
- 🔒 Secure authentication and verification
- 📄 Resume parsing and context-aware questioning
- 💬 WebSocket support for real-time communication

## Prerequisites

- Python 3.8+
- Node.js 16+
- Vapi.ai account
- Twilio account
- Deepgram account (optional for transcription)

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Vapi.ai Configuration
VAPI_SHARE_KEY=your_share_key
VAPI_PRIVATE_KEY=your_private_key
VAPI_ASSISTANT_ID=your_assistant_id
VAPI_BASE_URL=https://api.vapi.ai
VAPI_WEBHOOK_URL=your_webhook_url
VAPI_DESTINATION_NUMBER=your_phone_number

# Twilio Configuration
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_APP_SID=your_app_sid
TWILIO_PHONE_NUMBER=your_phone_number
TWILIO_VERIFY_SERVICE_SID=your_verify_service_sid

# Flask Configuration
FLASK_SECRET_KEY=your_secret_key
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/interview-app.git
cd interview-app
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Install Node.js dependencies:
```bash
npm install
```

## Running the Application

1. Start the Node.js transcription service:
```bash
npm start
```

2. In a separate terminal, start the Flask application:
```bash
python interview_app.py
```

The application will be available at `http://localhost:5000`

## Usage

1. **Starting an Interview**
   - Navigate to the home page
   - Enter candidate details and job information
   - Upload a resume (optional)
   - Choose between instant interview or scheduled call

2. **During the Interview**
   - The AI interviewer will conduct a natural conversation
   - Questions are dynamically generated based on the context
   - Real-time transcription is available
   - Interview progress is automatically saved

3. **Post-Interview**
   - Access interview transcripts
   - Review AI-generated feedback
   - Export interview data

## Architecture

The application consists of several key components:

- Flask backend for main application logic
- Node.js service for real-time transcription
- WebSocket integration for live communication
- Vapi.ai for AI conversation management
- Twilio for phone call handling

## Security

- All sensitive data is handled via environment variables
- Phone number verification through Twilio
- Secure WebSocket connections
- Session-based authentication
- Rate limiting on API endpoints

## Development

To run the application in development mode:

1. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

2. Start the application in debug mode:
```bash
python interview_app.py --debug
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Vapi.ai](https://vapi.ai) for AI conversation capabilities
- [Twilio](https://twilio.com) for telephony services
- [Deepgram](https://deepgram.com) for transcription services

## Support

For support, please open an issue in the GitHub repository or contact the development team.

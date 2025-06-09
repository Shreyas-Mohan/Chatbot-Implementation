# Chatbot-Implementation

This repository contains **two conversational AI chatbot projects**:

1. **Chatbot using Chainlit**  
2. **Chatbot using Telegram (aiogram)**

Both projects use Google's Gemini model via an OpenAI-compatible API endpoint as the backend LLM.

---

## 1. Chatbot using Chainlit

A conversational chatbot for order-taking (Zomato-style), built with [Chainlit](https://www.chainlit.io/) for an interactive chat UI.

### Features

- Conversational chatbot for restaurant ordering
- Uses Gemini model through OpenAI-compatible API endpoint
- System prompt and menu defined for a restaurant experience
- Easy-to-use web interface via Chainlit

### How it Works

- The backend uses the Gemini model by sending requests to the OpenAI-compatible endpoint:  
  `https://generativelanguage.googleapis.com/v1beta/openai/`
- The API key for Gemini is loaded from a `.env` file.
- The chatbot logic is implemented in Python, with Chainlit handling user interactions and message flow.

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Chatbot-Implementation.git
   cd Chatbot-Implementation
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your `.env` file**
   ```
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```
   > The code uses the OpenAI Python client, but points it to the Gemini OpenAI-compatible endpoint.

4. **Run the chatbot**
   ```bash
   chainlit run app.py
   ```
   The app will be available at [http://localhost:8000](http://localhost:8000).

---

## 2. Chatbot using Telegram (aiogram)

A Telegram chatbot that uses the Gemini model as its backend, built with [aiogram](https://docs.aiogram.dev/en/latest/).

### Features

- Telegram bot interface for chatting with Gemini
- Supports `/start` and `/clear` commands
- Maintains minimal context between turns
- Echo bot example also included for reference

### How it Works

- The bot receives messages from users on Telegram.
- Each message is sent to the Gemini model via the OpenAI-compatible API endpoint.
- The bot replies with the model's response.
- The API key and Telegram bot token are loaded from a `.env` file.

### Setup Instructions

1. **Create a Telegram bot** via [BotFather](https://t.me/botfather) and get your bot token.

2. **Set up your `.env` file** in the `Chatbot using telegram` folder:
   ```
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Telegram bot**
   ```bash
   python "Chatbot using telegram/mybot.py"
   ```

   For the echo bot example:
   ```bash
   python "Chatbot using telegram/trial/echo_bot.py"
   ```

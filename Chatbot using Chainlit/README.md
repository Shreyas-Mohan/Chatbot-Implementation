# Chatbot-Implementation-Using-Chainlit

This project is a conversational AI chatbot built using [Chainlit](https://www.chainlit.io/) as the frontend and Google's Gemini model via an OpenAI-compatible API endpoint as the backend LLM.

## Features

- Conversational chatbot for order-taking (Zomato-style)
- Uses Gemini model through OpenAI-compatible API endpoint
- Built with Chainlit for an interactive chat UI
- System prompt and menu defined for a restaurant ordering experience

## How it Works

- The backend uses the Gemini model by sending requests to the OpenAI-compatible endpoint:  
  `https://generativelanguage.googleapis.com/v1beta/openai/`
- The API key for Gemini is loaded from a `.env` file.
- The chatbot logic is implemented in Python, with Chainlit handling user interactions and message flow.

## Setup Instructions

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
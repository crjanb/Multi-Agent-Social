# Multi-Agent AI Social Media System

A production-quality multi-agent AI system that automatically researches a topic, generates content, creates visuals, and posts on X (Twitter).

## Features
- **Research Agent**: Uses Tavily to gather information on any topic.
- **Writer Agent**: Uses Groq (llama3-70b-8192) to generate viral tweet content.
- **Visual Agent**: Generates relevant images for the post.
- **Post Agent**: Automatically posts the content to X via the Twitter API.
- **LangGraph Orchestration**: Robust state management and agent coordination.
- **FastAPI Layer**: Exposes the system via a clean REST API.

## Project Structure
```text
ai_social_agent/
├── app/
│   ├── agents/         # Multi-agent logic
│   ├── controllers/    # Request handling and workflow triggers
│   ├── graph/          # LangGraph orchestration
│   ├── models/         # State definitions
│   ├── routes/         # API endpoints
│   ├── services/       # External service integrations (LLM, Image, Social)
│   ├── tools/          # Utilities and search tools
│   └── utils/          # Config and logging
├── main.py             # Entry point
├── .env                # Secret management
└── requirements.txt    # Dependencies
```

## Setup Instructions

1. **Create Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Copy `.env.example` to `.env` and fill in your API keys:
   - `GROQ_API_KEY`
   - `TAVILY_API_KEY`
   - `X_API_KEY`, `X_API_SECRET`, etc.

4. **Run the Application**:
   ```bash
   python main.py
   ```

## API Usage

### Generate and Post
`POST /api/generate-post`

**Body**:
```json
{
  "topic": "The future of AI agents in 2024"
}
```

**Response**:
```json
{
  "tweet": "...",
  "image_path": "...",
  "post_url": "...",
  "status": "success"
}
```

## Tech Stack
- **Python**
- **FastAPI**
- **LangChain & LangGraph**
- **Groq LLM API**

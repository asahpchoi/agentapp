# Business Role Generator and Discussion Platform

A FastAPI-based web application that generates business roles using OpenAI's GPT model and facilitates business plan discussions.

## Project Structure
```
/
├── api.py              # Main FastAPI application
├── static/            # Static files directory
│   ├── index.html     # Main web interface
│   ├── styles.css     # CSS styles
│   └── scripts.js     # JavaScript functionality
├── requirements.txt   # Python dependencies
└── .env              # Environment variables
```

## Features

### 1. Role Generation
- Generate 1-5 business roles based on a given topic
- Each role includes a title, description, and instruction
- Uses OpenAI's GPT model for generation

### 2. Role Management
- Save generated roles to Supabase database
- View saved roles
- Start discussions with generated roles

### 3. Chat Interface
- Interact with generated roles
- Discuss business strategies
- View chat history

## API Endpoints

### 1. Basic Utility
- `GET /echo/{message}`: Echo test endpoint
- `GET /chat/{message}`: Chat with agents
- `GET /code/{prompt}`: Generate code

### 2. Database Operations
- `POST /messages`: Save chat messages
- `POST /save_roles`: Save generated roles

### 3. Role Generation and Discussion
- `POST /generate_roles`: Generate business roles
- `POST /start_talk`: Start a discussion

## Setup

### 1. Environment Variables Required
- `SUPABASE_URL`: Supabase project URL
- `SUPABASE_KEY`: Supabase API key
- `AZURE_API_KEY`: Azure OpenAI API key

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Run the Application
```sh
uvicorn api:app --reload
```

## Usage

### 1. Generate Roles
- Enter a business topic
- Specify number of roles (1-5)
- Click "Generate Roles"

### 2. Save Roles
- Review generated roles
- Click "Save Roles" to store in database

### 3. Start Discussion
- Click "Start Discussion" with saved roles
- Enter messages to interact with roles
- View responses in chat section

## Technical Details

### 1. Frontend
- HTML5, CSS3, JavaScript
- Fetch API for backend communication
- Dynamic content rendering

### 2. Backend
- FastAPI framework
- Pydantic for data validation
- OpenAI integration for role generation
- Supabase for data storage

### 3. Data Models
- `AgentRole`: title, description, instruction
- `TopicRequest`: topic, numRoles
- `SaveRolesRequest`: topic, roles[]
- `Message`: content

## Error Handling
- Input validation for all endpoints
- Detailed error logging
- User-friendly error messages
- Exception handling for API calls

## Dependencies
- fastapi
- uvicorn
- openai
- supabase
- python-dotenv
- pydantic

Note: See `requirements.txt` for complete list with versions.

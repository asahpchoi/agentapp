import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from autogen_api import chat_with_agents, generate_code_with_agent
from pydantic import BaseModel
from typing import List
 
from openai import AzureOpenAI
import logging
import json

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AgentRole(BaseModel):
    title: str
    description: str

class BusinessRolesResponse(BaseModel):
    roles: List[AgentRole]

class TopicRequest(BaseModel):
    topic: str

@app.get("/echo/{message}")
async def echo(message:str):
    return message

@app.get("/chat/{message}")
async def chat(message: str):
    print("calling chat")
    return await chat_with_agents(message)

@app.get("/code/{prompt}")
async def generate_code(prompt: str):
    return await generate_code_with_agent(prompt)

@app.post("/generate_roles", response_model=BusinessRolesResponse)
async def generate_roles(request: TopicRequest):
    if not request.topic:
        raise HTTPException(status_code=400, detail="Topic cannot be empty")

    """
        "model": "gpt-4",
        "api_key": os.getenv("AZURE_API_KEY"),
        "base_url": "https://ik-oai-eastus-2.openai.azure.com",
        "api_type": "azure",
        "api_version": "2024-02-01"
    """    
 
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_API_KEY"),  
        api_version="2024-02-01",
        azure_endpoint="https://ik-oai-eastus-2.openai.azure.com"
    )
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates JSON responses. Always ensure your response is valid JSON."},
                {"role": "user", "content": f"""Generate 5 agent roles with descriptions for discussing a business plan for a {request.topic}. 
                Return the response in this exact JSON format:
                [
                    {{"role": "Role Name 1", "description": "Role Description 1"}},
                    {{"role": "Role Name 2", "description": "Role Description 2"}},
                    ...
                ]"""}
            ],
            max_tokens=500,
            n=1,
            temperature=0.7,
        )
    except Exception as e:
        logging.error(f"OpenAI API call failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"OpenAI API call failed: {str(e)}")
    
    response_content = response.choices[0].message.content.strip()
    logging.info(f"OpenAI response content: {response_content}")
    
    try:
        roles_data = json.loads(response_content)
        roles = [AgentRole(title=role["role"], description=role["description"]) for role in roles_data]
    except (json.JSONDecodeError, KeyError) as e:
        logging.error(f"Failed to parse roles: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to parse roles: {str(e)}")
    
    return BusinessRolesResponse(roles=roles)

# Mount static files after API routes
app.mount("/", StaticFiles(directory="static", html=True), name="static")

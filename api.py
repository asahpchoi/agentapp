import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
 
from pydantic import BaseModel
from typing import List
from openai import AzureOpenAI
import logging
import json
from supabase import create_client, Client

app = FastAPI()

# Initialize Supabase client
supabase: Client = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

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
    instruction: str

class BusinessRolesResponse(BaseModel):
    roles: List[AgentRole]

class TopicRequest(BaseModel):
    topic: str
    numRoles: int

class Message(BaseModel):
    content: str

class SaveRolesRequest(BaseModel):
    topic: str
    roles: List[AgentRole]

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

@app.post("/messages", response_model=dict)
async def create_message(message: Message):
    try:
        # Insert the message into the messages table
        data = supabase.table('messages').insert({"content": message.content}).execute()
        return {"status": "success", "data": data.data}
    except Exception as e:
        logging.error(f"Failed to insert message: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to insert message: {str(e)}")

@app.post("/save_roles", response_model=dict)
async def save_roles(request: SaveRolesRequest):
    try:
        # Insert the roles into the business_roles table
        roles_data = []
        for role in request.roles:
            role_entry = {
                "topic": request.topic,
                "title": role.title,
                "description": role.description,
                "instruction": role.instruction
            }
            roles_data.append(role_entry)
        
        data = supabase.table('business_roles').insert(roles_data).execute()
        return {"status": "success", "data": data.data}
    except Exception as e:
        logging.error(f"Failed to save roles: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to save roles: {str(e)}")

@app.post("/generate_roles", response_model=BusinessRolesResponse)
async def generate_roles(request: TopicRequest):
    if not request.topic:
        raise HTTPException(status_code=400, detail="Topic cannot be empty")
    if not (1 <= request.numRoles <= 5):
        raise HTTPException(status_code=400, detail="Number of roles must be between 1 and 5")
 
    #print(request)
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
                {"role": "user", "content": f"""Generate {request.numRoles} agent roles with descriptions and instructions for discussing a business plan for a {request.topic}. 
                Return the response in this exact JSON format:
                [
                    {{"role": "Role Name 1", "description": "Role Description 1", "instruction": "Role Instruction 1"}},
                    {{"role": "Role Name 2", "description": "Role Description 2", "instruction": "Role Instruction 2"}},
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
    #print(response.choices[0].message.content)
    response_content = response.choices[0].message.content.strip()
    logging.info(f"OpenAI response content: {response_content}")
    
    try:
        roles_data = json.loads(response_content)
        roles = [AgentRole(title=role["role"], description=role["description"], instruction=role["instruction"]) for role in roles_data]
        print(roles)
    except (json.JSONDecodeError, KeyError) as e:
        logging.error(f"Failed to parse roles: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to parse roles: {str(e)}")
    
    return BusinessRolesResponse(roles=roles)


def talk(topic, agents):
    api_base = "https://ik-oai-eastus-2.openai.azure.com"
    api_key= "b3e819600fbe4981be34ef2aa79943e2"
    deployment_name = 'gpt-4o'
    api_version = '2024-02-01' # this might change in the future
    from autogen import ConversableAgent, GroupChat, GroupChatManager
    conf =  {
        "model": deployment_name,
        "api_key": api_key,
        "base_url": api_base,
        "api_type": "azure",
        "api_version": api_version
    }
    conversable_agents = []

    llm_config = {
    'config_list': [conf]
    }

    for agent_data in agents:
 
 
        agent = ConversableAgent(
            name=agent_data.title,
            llm_config=llm_config,
            system_message=agent_data.description
        )

        agent_instance = {
            'recipient': agent,
            'message': agent_data.instruction + f" context: {topic}",
            'max_turns': 1,
            'summary_method': 'last_msg',
        }

        conversable_agents.append(agent_instance)
 
    manager = ConversableAgent(
        'Founder',
        llm_config=llm_config,
        system_message=f'We start a conversation for {topic}',
        human_input_mode='NEVER',
    )

    response = manager.initiate_chats(conversable_agents)
    return response

@app.post("/start_talk", response_model=str)
async def start_talk(request: SaveRolesRequest):
    try:
        #logging.info(f"StartTalk request payload: {request.json()}")
        # Call the StartTalk API with the roles and topic
         
        response = talk(request.topic, request.roles)
        return response
    except Exception as e:
        #logging.error(f"Failed to start talk: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to start talk: {str(e)}")

# Mount static files after API routes
app.mount("/", StaticFiles(directory="static", html=True), name="static")

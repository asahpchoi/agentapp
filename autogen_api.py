import os
from autogen import ConversableAgent
from autogen.coding import LocalCommandLineCodeExecutor
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

azure_model = {
    "model": "gpt-4",
    "api_key": os.getenv("AZURE_API_KEY"),
    "base_url": "https://ik-oai-eastus-2.openai.azure.com",
    "api_type": "azure",
    "api_version": "2024-02-01"
}

code_writer_system_message = """You are a helpful AI assistant.
you are experience coder in vite and nodejs
always build the full app and execution
"""

code_writer_agent = ConversableAgent(
    "code_writer_agent",
    system_message=code_writer_system_message,
    llm_config={"config_list": [azure_model]},
    code_execution_config=False,
)

executor = LocalCommandLineCodeExecutor(
    timeout=10,
    work_dir=".",
)

code_executor_agent = ConversableAgent(
    "code_executor_agent",
    llm_config=False,
    code_execution_config={"executor": executor},
    human_input_mode="ALWAYS",
)

sa_agent = ConversableAgent(
    name="CEO",
    system_message="You are a CEO of a fortune 500 company, who specialized in making direction and work in medical business",
    llm_config={"config_list": [azure_model]},
)

ba_agent = ConversableAgent(
    name="Growth_Hacker",
    system_message="You are a growth hacker, and you are good at providing ideas for business growth with 5 years plan",
    llm_config={"config_list": [azure_model]},
)

async def chat_with_agents(message: str):
    try:
        print(message)
        # Start a chat between CEO and Growth Hacker
        chat_result = await sa_agent.a_initiate_chat(
            ba_agent,
            message=message,
            silent=True
        )
        
        # Extract the last message from the conversation
        last_message = chat_result.last_message()
        return {"result": last_message.get("content", "No response generated")}
    except Exception as e:
        return {"error": str(e)}

async def generate_code_with_agent(prompt: str):
    try:
        # Generate code using the code writer agent
        code_result = await code_writer_agent.a_initiate_chat(
            code_executor_agent,
            message=prompt,
            silent=True
        )
        
        # Extract the last message from the conversation
        last_message = code_result.last_message()
        return {"result": last_message.get("content", "No code generated")}
    except Exception as e:
        return {"error": str(e)}

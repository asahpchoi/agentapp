import json
from autogen import ConversableAgent, GroupChat, GroupChatManager

def start_discussion(topic, agents):
    """
    topic:
    agents:

    """
    api_base = "https://ik-oai-eastus-2.openai.azure.com"
    api_key= "b3e819600fbe4981be34ef2aa79943e2"
    deployment_name = 'gpt-4o'
    api_version = '2024-02-01' # this might change in the future
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
            name=agent_data.title,  # Using dot notation for Pydantic model
            llm_config=llm_config,
            system_message=agent_data.description,  # Using dot notation for Pydantic model
            silent=True,
        )

        agent_instance = {
            'recipient': agent,
            'message': agent_data.instruction + f" context: {topic}",  # Using dot notation for Pydantic model
            'max_turns': 1,
            'summary_method': 'last_msg',
             
        }

        conversable_agents.append(agent_instance)
 
    manager = ConversableAgent(
        'Founder',
        llm_config=llm_config,
        system_message=f'We start a conversation for {topic}',
        human_input_mode='NEVER',
        silent=True,
    )

    chat_history = manager.initiate_chats(conversable_agents)
    
    # Capture chat history
    #chat_history = manager.get_chat_history()
    
    # Convert the response to a string format
    return   chat_history

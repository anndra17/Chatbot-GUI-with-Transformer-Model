from langchain.chains import ConversationChain  
from langchain.memory import ConversationBufferMemory
from langchain.llms import HuggingFacePipeline
from transformers import pipeline


# Set up the Hugging Face model 
chatbot =  pipeline("text2text-generation", model="google/flan-t5-large")

# Set up Langchain with the Hugging Face pipeline
llm = HuggingFacePipeline(pipeline=chatbot)

# Create a conversation chain
memory = ConversationBufferMemory(clear_after_n=10)  # reset history after 10 interactions
conversation = ConversationChain(llm=llm)

def truncate_input(user_input, max_tokens=256):
    # Truncate the input to avoid exceeding the limits
    tokens = user_input.split()
    return " ".join(tokens[:max_tokens])


def get_response(user_input):
    if not user_input.strip(): # Check if the input is empty or just spaces
        return "Please enter a valid message."
    response = conversation.predict(input=user_input)
    return response





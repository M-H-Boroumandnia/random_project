import logging
from divar_client import DivarKenarChat
from schemas import Message

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def main():
    try:
        # Initialize client
        chat_client = DivarKenarChat()
        
        print("\n===== TESTING CONVERSATION START =====")
        # Start new conversation
        new_message = Message(text="Hello, is this available?")
        response = chat_client.start_conversation(
            post_token="POST_TOKEN_FROM_DIVAR",  # Replace with actual token
            message=new_message
        )
        print("New Conversation ID:", response.get('conversation_id'))
        
    except Exception as e:
        print(f"\n❌ Critical Error: {str(e)}")
        print("Check your .env file for DIVAR_API_KEY and verify your post token")

if __name__ == "__main__":
    main()
from ai_engine.chitchat import ChitChatDialogue
from ai_engine.messages import DialogueMessage
from uuid import uuid4
from datetime import datetime

# Initialize the agent and dialogue
chitchat_dialogue = ChitChatDialogue(version="0.1", storage=None)

# Simulate a dialogue session
message = DialogueMessage(
    message_id=uuid4(),
    timestamp=datetime.now(),
    type="user_message",
    user_message="Hello, AI!"
)

# Start and continue the dialogue
chitchat_dialogue.on_start_dialogue(model=message)
chitchat_dialogue.on_continue_dialogue(model=message)

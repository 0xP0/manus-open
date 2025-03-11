from langchain_core.messages import BaseMessage
import json

def convert_input_messages(messages: list[BaseMessage], model_name: str) -> list[BaseMessage]:
    return messages


# extract_json_from_model_output

def extract_json_from_model_output(content: str) -> dict:
    return json.loads(content)


def save_conversation(conversation: list[BaseMessage], file_path: str) -> None:
    with open(file_path, 'w') as f:
        for message in conversation:
            f.write(message.to_string() + '\n')



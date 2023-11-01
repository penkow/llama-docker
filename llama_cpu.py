from llama_cpp import Llama

# Put the location of to the GGUF model that you've download from HuggingFace here
model_path = "**path to the GGUF file**"

# Create a llama model
model = Llama(model_path=model_path)

# Prompt creation
system_message = "You are a helpful assistant"
user_message = "Generate a list of 5 funny dog names"

prompt = f"""<s>[INST] <<SYS>>
{system_message}
<</SYS>>
{user_message} [/INST]"""

# Model parameters
max_tokens = 100

# Run the model
output = model(prompt, max_tokens=max_tokens, echo=True)

# Print the model output
print(output)
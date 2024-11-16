from transformers import GPT3LMHeadModel, GPT3Tokenizer

# Load pre-trained model and tokenizer
model_name = "gpt3"
model = GPT3LMHeadModel.from_pretrained(model_name)
tokenizer = GPT3Tokenizer.from_pretrained(model_name)

def generate_feedback(user_answer):
    # Encode user input to model's input format
    inputs = tokenizer.encode(user_answer, return_tensors='pt')
    
    # Generate response from the model
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2)

    # Decode the model's output to text
    feedback = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return feedback

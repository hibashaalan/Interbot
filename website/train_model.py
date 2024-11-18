from datasets import load_dataset
from transformers import GPT3LMHeadModel, GPT3Tokenizer
from transformers import Trainer, TrainingArguments

# Load the dataset (ensure the correct format)
dataset = load_dataset("behavioral.html")  # Modify with actual dataset path

# Load the pre-trained model and tokenizer
model_name = "gpt2"  # Replace with the correct model
model = GPT3LMHeadModel.from_pretrained(model_name)
tokenizer = GPT3Tokenizer.from_pretrained(model_name)

# Preprocess the dataset
def preprocess_function(examples):
    return tokenizer(examples['answer'], truncation=True, padding='max_length', max_length=512)

encoded_dataset = dataset.map(preprocess_function, batched=True)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=3,
    logging_dir='./logs',
    save_steps=500,
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=encoded_dataset['train'],
    eval_dataset=encoded_dataset['test'],
)

# Start training
trainer.train()

# Save the model after training
model.save_pretrained("./fine_tuned_model")
tokenizer.save_pretrained("./fine_tuned_model")

print("Model training complete!")

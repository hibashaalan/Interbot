from datasets import load_dataset
from transformers import GPT3LMHeadModel, GPT3Tokenizer
from transformers import Trainer, TrainingArguments

# Load dataset 
dataset = load_dataset("behavioral.html")

# Load the pre-trained model and tokenizer
model_name = "gpt3"  
model = GPT3LMHeadModel.from_pretrained(model_name)
tokenizer = GPT3Tokenizer.from_pretrained(model_name)

# Preprocess the dataset: tokenizing the answers and feedback
def preprocess_function(examples):
    return tokenizer(examples['answer'], truncation=True, padding='max_length', max_length=512)

# Apply preprocessing to the dataset
encoded_dataset = dataset.map(preprocess_function, batched=True)

# Define the training arguments
training_args = TrainingArguments(
    output_dir="./results",            # Where to save the model
    evaluation_strategy="epoch",       # Evaluate after each epoch
    per_device_train_batch_size=4,     # Batch size for training
    per_device_eval_batch_size=4,      # Batch size for evaluation
    num_train_epochs=3,                # Number of training epochs
    logging_dir='./logs',              # Directory for logging
    logging_steps=10,
    save_steps=500,                    # Save model checkpoint every 500 steps
    warmup_steps=200,                  # Gradual learning rate warm-up steps
    weight_decay=0.01,                 # Weight decay for regularization
    load_best_model_at_end=True,       # Load the best model based on evaluation metric
)

# Initialize the Trainer
trainer = Trainer(
    model=model,                       # The pre-trained model you want to fine-tune
    args=training_args,                # The training configuration
    train_dataset=encoded_dataset['train'],  # Your training data
    eval_dataset=encoded_dataset['test'],    # Your evaluation data
)

# Start training
trainer.train()

# Save the model after training
model.save_pretrained("./fine_tuned_model")
tokenizer.save_pretrained("./fine_tuned_model")

print("Analysis complete!")

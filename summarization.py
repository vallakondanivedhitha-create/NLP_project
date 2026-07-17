from transformers import pipeline
print("Loading the summarization pipeline...")
summarizer = pipeline(
    "summarization", 
    model="facebook/bart-large-cnn"
    )
print("Summarization pipeline loaded successfully!")
print("Enter 'exit' to quit the summarization tool.\n")
while True:
    text=input("Enter text to summarize: ")
    if text.lower() == "exit":
        print("Exiting the summarization tool. Goodbye!")
        break
    summary = summarizer(
        text, 
        max_length=130, 
        min_length=30, 
        do_sample=False
        )
    print(f"Summary: {summary[0]['summary_text']}\n")
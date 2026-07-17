from transformers import pipeline
print("Loading the question-answering pipeline...")
qa_pipeline = pipeline(
    "question-answering",
    model="distilbert-base-uncased-distilled-squad",
    framework="pt"   # Force PyTorch
)
print("Pipeline Loaded Successfully")

# Generate the context
context = """ Python is a high-level programming language created by Guido van Rossum in 1991.

Python is simple, readable, and easy to learn.

It supports object-oriented programming, functional programming,
and procedural programming.

Python is widely used in Artificial Intelligence,
Machine Learning, Deep Learning,
Data Science, Web Development,
Automation, Cyber Security, and Game Development.

Popular Python libraries include NumPy,
Pandas, Matplotlib, TensorFlow,
PyTorch, Scikit-learn, and OpenCV.

TensorFlow was developed by Google.

PyTorch was developed by Facebook.

Python files use the .py extension. """

print("Q/A Chatbot___!\n")
print("Enter 'exit' to quit the chatbot.\n")

while True:
    question = input("You: ")
    if question.lower() == "exit":
        print("Exiting the chatbot.Goodbye!")
        break
    result = qa_pipeline(question = question , context = context)
    answer = result['answer']
    print(f"Chatbot: {answer}\n")

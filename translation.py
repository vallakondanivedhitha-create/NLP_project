from transformers import pipeline
print("Loading the translation pipeline...")
translation_pipeline = pipeline(
    "translation_en_to_fr",
    model="Helsinki-NLP/opus-mt-en-fr"
)

print("English to French translation pipeline loaded successfully!")
print("Enter text to translate or 'exit' to quit the translation tool.\n")
while True:
    text = input("Enter text to translate: ")
    if text.lower() == "exit":
        print("Exiting the translation tool. Goodbye!")
        break
    else:
        translation = translation_pipeline(text,max_length=400)
        print("Translation: ", translation[0]['translation_text'], "\n")
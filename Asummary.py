import pickle
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

def save_model_and_tokenizer(model, tokenizer, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump((model, tokenizer), f)

def load_model_and_tokenizer(file_name):
    with open(file_name, 'rb') as f:
        model, tokenizer = pickle.load(f)
    return model, tokenizer

def summarize_text(text, model, tokenizer):
    tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")
    summary = model.generate(**tokens)
    return tokenizer.decode(summary[0])

if __name__ == '__main__':
    tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
    model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")
    save_model_and_tokenizer(model, tokenizer, 'model.pkl')

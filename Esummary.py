import pickle
from summarizer import Summarizer

def save_model(model, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(model, f)

def load_model(file_name):
    with open(file_name, 'rb') as f:
        model = pickle.load(f)
    return model

def summarize_text(text, model):
    result = model(text, ratio=0.5)
    summarized_text = ''.join(result)
    return summarized_text

if __name__ == '__main__':
    model = Summarizer()
    save_model(model, 'summarizer_model.pkl')

# Next Word Prediction
Experiment on the Generative Pretrained Transformer 2 (GPT-2) for Language Modeling task using the PyTorch-Transformers library.

## Installation
Requires python>=3.5, pytorch>=1.6.0, pytorch-transformers>=1.2.0
```bash
pip install next-word-prediction
```

## How to use
```python
>>> from next_word_prediction import GPT2
>>> gpt2 = GPT2()
>>> text = "The course starts next"
>>> gpt2.predict_next(text)
The course starts next ['week', 'to', 'month', 'year', 'Monday']
```

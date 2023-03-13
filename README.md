# Text Summarizer with NLP

This project generates a summary of a given text using natural language processing (NLP) methods. It makes use of the nltk and spacy libraries for text processing and analysis.

## Installation
Before running the project, you need to install the necessary dependencies. You can do this using pip, the Python package manager.

First, install the nltk library by running the following command in your terminal:

```bash
pip install nltk
pip install spacy
```
Next, download the punkt dataset from the nltk library by running the following command:

```bash
python -m nltk.downloader punkt
```
Finally, install the spacy library and the en_core_web_sm model by running the following commands:

```cpp
python -m spacy download en_core_web_sm
```
## Usage Example
### Input[1]
```python
text = """The weather today is sunny with a few clouds.
The temperature is around 20 degrees Celsius.
The wind speed is about 10 kilometers per hour."""

sentences, keywords = summarize(text)

print("Summarized Sentences:")
for sentence in sentences:
    print("- " + sentence)

print("\nKeywords:")
for keyword in keywords:
    print("- " + keyword)
```
### Output[1]

```bash
Summarized Sentences:
- The weather today is sunny with a few clouds.
- The temperature is around 20 degrees Celsius.
- The wind speed is about 10 kilometers per hour.

Keywords:
- weather
- today
- sunny
- clouds
- temperature
```

### Input[2]
```python
text = """Artificial intelligence (AI) is the simulation of human intelligence processes by computer systems. These processes include 
learning (the acquisition of information and rules for using the information), reasoning (using rules to reach approximate or definite 
conclusions), and self-correction. AI is a rapidly developing field, with technological advances and new research expanding the field 
every day. The possibilities of AI are vast and diverse, ranging from self-driving cars and facial recognition technology to medical 
diagnosis and personalized medicine. Despite its potential benefits, however, AI also poses new challenges and ethical questions, 
such as the potential for biased algorithms and the impact on the job market. As AI continues to advance, it is important for researchers 
and developers to consider the implications of their work and strive to create AI systems that are both effective and ethical."""

sentences, keywords = summarize(text)

print("Summarized Sentences:")
for sentence in sentences:
    print("- " + sentence)

print("\nKeywords:")
for keyword in keywords:
    print("- " + keyword)

```
### Output[2]

```bash
Summarized Sentences:
- Artificial intelligence (AI) is the simulation of human intelligence processes by computer systems.
- These processes include learning (the acquisition of information and rules for using the information),
  reasoning (using rules to reach approximate or definite conclusions), and self-correction.
- AI is a rapidly developing field, with technological advances and new research expanding the field every day.
- The possibilities of AI are vast and diverse, ranging from self-driving cars and facial recognition technology
  to medical diagnosis and personalized medicine.
- Despite its potential benefits, however, AI also poses new challenges and ethicalquestions, 
  such as the potential for biased algorithms and the impact on the job market.

Keywords:
- Artificial
- intelligence
- AI
- simulation
- human
```



## Contributing
This project is open source and contributions are welcome. A list of to-do items can be found on the project's GitHub page.

## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License. See the LICENSE file for more information.
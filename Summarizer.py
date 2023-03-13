import nltk
import spacy

nltk.download('punkt')
nlp = spacy.load('en_core_web_sm')


def summarize(text):
    sentences = nltk.sent_tokenize(text)
    doc = nlp(text)
    keywords = [
        token.text for token in doc if not token.is_stop and token.is_alpha]
    return sentences[:5], keywords[:5]

# Example 1
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


# Example 2
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



import string
from collections import Counter
import matplotlib.pyplot as plt

# Function to preprocess and analyze text
def analyze_text(file_path):
    try:
        
        with open(file_path, encoding="utf-8") as file:
            text = file.read()

        
        lower_case = text.lower()

        cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

        tokenized_words = cleaned_text.split()

        # Remove stop words
        stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]  
        
        final_words = [word for word in tokenized_words if word not in stop_words]

        
        emotion_list = []
        with open('emotions.txt', 'r') as emotion_file:
            for line in emotion_file:
                clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
                word, emotion = clear_line.split(':')
                if word in final_words:
                    emotion_list.append(emotion)

        return emotion_list

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

emotion_list = analyze_text("read.txt")


emotion_counts = Counter(emotion_list)

bar_colors = ['skyblue', 'lightcoral', 'lightgreen', 'violet', 'gold']
pie_colors = ['lightblue', 'lightcoral', 'lightgreen', 'violet', 'gold']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.bar(emotion_counts.keys(), emotion_counts.values(), color=bar_colors)
ax1.set_xlabel('Emotions')
ax1.set_ylabel('Frequency')
ax1.set_title('Emotion Analysis')

ax2.pie(emotion_counts.values(), labels=emotion_counts.keys(), autopct='%1.1f%%', startangle=90, colors=pie_colors)
ax2.axis('equal')
ax2.set_title('Emotion Distribution')

plt.savefig('graph.png')
plt.show()
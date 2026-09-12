import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense


# Dataset
sentences = [
    "I love this movie",
    "This movie is excellent",
    "I enjoyed the movie",
    "The movie was fantastic",
    "I like this film",

    "I hate this movie",
    "This movie is terrible",
    "I disliked the movie",
    "The movie was boring",
    "I do not like this film"
]

# 1 = Positive, 0 = Negative
labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]


# Tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)

sequences = tokenizer.texts_to_sequences(sentences)


# Padding
X = pad_sequences(sequences, maxlen=6, padding='post')

y = np.array(labels)


# Create LSTM model
model = Sequential()

model.add(
    Embedding(
        input_dim=len(tokenizer.word_index) + 1,
        output_dim=16,
        input_length=6
    )
)

model.add(LSTM(32))

model.add(Dense(1, activation='sigmoid'))


# Compile model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)


# Train model
model.fit(X, y, epochs=100, verbose=1)


# Test new sentence
new_sentence = ["I love this film"]

new_sequence = tokenizer.texts_to_sequences(new_sentence)

new_padded = pad_sequences(
    new_sequence,
    maxlen=6,
    padding='post'
)


# Prediction
prediction = model.predict(new_padded)

print("Prediction value:", prediction[0][0])


if prediction[0][0] >= 0.5:
    print("Positive Sentiment")
else:
    print("Negative Sentiment")

# =====================================================
# PRACTICAL: SMS SPAM CLASSIFICATION
# USING TF-IDF AND NAIVE BAYES
# =====================================================


# =====================================================
# STEP 1: IMPORT LIBRARIES
# =====================================================

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# =====================================================
# STEP 2: LOAD DATASET
# =====================================================

df = pd.read_csv(
    "spam.csv",
    encoding="latin-1"
)


# Display first 5 rows

print("FIRST 5 ROWS")

print(df.head())


# =====================================================
# STEP 3: CHECK COLUMN NAMES
# =====================================================

print("\nCOLUMN NAMES")

print(df.columns)


# =====================================================
# STEP 4: KEEP ONLY REQUIRED COLUMNS
# =====================================================

df = df[["v1", "v2"]]


# Rename columns

df.columns = [
    "label",
    "message"
]


# =====================================================
# STEP 5: CHECK DATASET INFORMATION
# =====================================================

print("\nDATASET SHAPE")

print(df.shape)


print("\nMISSING VALUES")

print(df.isnull().sum())


print("\nCLASS DISTRIBUTION")

print(df["label"].value_counts())


# =====================================================
# STEP 6: SEPARATE INPUT AND OUTPUT
# =====================================================

X = df["message"]

y = df["label"]


# =====================================================
# STEP 7: TRAIN-TEST SPLIT
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    # 20% for testing
    test_size=0.2,

    # Same result every time
    random_state=42,

    # Maintain class distribution
    stratify=y
)


# =====================================================
# STEP 8: TF-IDF VECTORIZATION
# =====================================================

# Create vectorizer

vectorizer = TfidfVectorizer()


# Learn vocabulary from training data
# and convert training text into numbers

X_train_tfidf = vectorizer.fit_transform(
    X_train
)


# Convert testing text using
# the same vocabulary

X_test_tfidf = vectorizer.transform(
    X_test
)


# =====================================================
# STEP 9: CREATE NAIVE BAYES MODEL
# =====================================================

model = MultinomialNB()


# =====================================================
# STEP 10: TRAIN MODEL
# =====================================================

model.fit(
    X_train_tfidf,
    y_train
)


# =====================================================
# STEP 11: MAKE PREDICTIONS
# =====================================================

y_pred = model.predict(
    X_test_tfidf
)


# =====================================================
# STEP 12: ACTUAL VS PREDICTED
# =====================================================

results = pd.DataFrame({

    "Actual": y_test.values,

    "Predicted": y_pred
})


print("\nACTUAL VS PREDICTED")

print(results.head(10))


# =====================================================
# STEP 13: ACCURACY
# =====================================================

accuracy = accuracy_score(
    y_test,
    y_pred
)


print("\nMODEL ACCURACY")

print(accuracy)


print("\nACCURACY PERCENTAGE")

print(accuracy * 100)


# =====================================================
# STEP 14: CLASSIFICATION REPORT
# =====================================================

print("\nCLASSIFICATION REPORT")

print(

    classification_report(
        y_test,
        y_pred
    )
)


# =====================================================
# STEP 15: CONFUSION MATRIX
# =====================================================

cm = confusion_matrix(
    y_test,
    y_pred
)


print("\nCONFUSION MATRIX")

print(cm)


# =====================================================
# STEP 16: TEST A NEW MESSAGE
# =====================================================

new_message = [

    "Congratulations you have won a free prize"
]


# Convert message into TF-IDF

new_message_tfidf = vectorizer.transform(
    new_message
)


# Predict

prediction = model.predict(
    new_message_tfidf
)


print("\nNEW MESSAGE")

print(new_message[0])


print("\nPREDICTION")

print(prediction[0])
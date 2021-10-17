import json
import random
import numpy as np
import nltk
import pickle

#import tflearn as tflearn
import tflearn
from nltk.stem.lancaster import LancasterStemmer
import tensorflow

stemmer = LancasterStemmer()

with open("ChatBot.json") as file:
    intents = json.load(file)
#intents = json.loads(open("ChatBot.json").read())

print(intents)

try:
    # Uncomment the next line to run the except if any changes occur in JSON file
    # x
    with open("data.pickle", "rb") as f:
        words, classes, training, output = pickle.load(f)

except:
    words = []
    classes = []
    documents_x = []
    documents_y =[]
    ignore_letters = []

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            word_list = nltk.word_tokenize(pattern)
            words.extend(word_list)
            documents_x.append(word_list)
            documents_y.append(intent["tag"])
            if intent["tag"] not in classes:
                classes.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w not in "?"]
    words = sorted(set(words))

    classes = sorted(classes)

    pickle.dump(words, open("words.pkl", "wb"))
    pickle.dump(words, open("classes.pkl", "wb"))

    training = []
    output = []
    output_empty = [0 for _ in range(len(classes))]

    for x,document in enumerate(documents_x):
        bag =[]
        word_patterns = [stemmer.stem(w) for w in document]

        for word in words:
            if word in word_patterns:
                bag.append(1)
            else:
                bag.append(0)
        output_row = output_empty[:]
        output_row[classes.index(documents_y[x])] = 1
        training.append(bag)
        output.append(output_row)

    training = np.array(training)
    output = np.array(output)
    with open("data.pickle", "wb") as f:
        pickle.dump((words,classes, training,output), f)

net = tflearn.input_data(shape=[None,len(training[0])])
net = tflearn.fully_connected(net,8)
net = tflearn.fully_connected(net,8)
net = tflearn.fully_connected(net,len(output[0]), activation = "softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    model.load("chatbot_model.model")
except:

    model.fit(training, output, n_epoch=1000, batch_size = 8, show_metric=True)
    model.save("chatbot_model.model")

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i,w in enumerate(words):
            if w==se:
                if w == se:
                    bag[i] = (1)
    return np.array(bag)

def chat():
    print("Start talking with the bot!")
    while True:
        inp = input("You: ")
        if inp.lower()=="quit":
            break
        results = model.predict([bag_of_words(inp,words)])
        results_index = np.argmax(results)
        tag = classes[results_index]
        if results[results_index] > 0.7:
            for tg in intents["intents"]:
                if tg["tag"] == tag:
                    responses =  tg["responses"]
            print(random.choice(responses))
        else:
            print("I didn't get that, try again please.")


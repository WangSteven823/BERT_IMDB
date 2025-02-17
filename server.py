#!/usr/bin/env python
# coding: utf-8

# In[1]:


from transformers import pipeline
from flask import Flask, request, render_template, jsonify


model_name = "./model/bert-finetuned-pretrained-imdb-sentiment/"
app = Flask(__name__, template_folder= "./templates/")
    
@app.route('/')
def text():
    return render_template("review.html") 
    
@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        movie_review = request.form['review']
        token_classifier = pipeline(
            "text-classification",
            model=model_name,
            tokenizer=model_name,
            padding=True,
            truncation=True,
            device="cuda"
        )
        response = token_classifier(movie_review)[0]
        print("post : review => ", movie_review)
        print(response)
        return jsonify({"評論": movie_review, "類別": response["label"], "分數": response["score"]})
    else:
        print("get : review => ", movie_review)
        return jsonify(movie_review)

if __name__ == '__main__':
    app.run()
    


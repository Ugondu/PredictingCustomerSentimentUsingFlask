from flask import Flask, request, jsonify
import joblib

app = Flask('my_app')

# Load model and vectorizer

vectorizer = joblib.load(r"C:\Users\ADACHUKWU\Desktop\ALL DATA SCIENCE\Internship\vectorizer.joblib")
model = joblib.load(r"C:\Users\ADACHUKWU\Desktop\ALL DATA SCIENCE\Internship\SVC.pkl")

@app.route('/analyze',methods = ['POST'])
def analyze():
    text = request.form['text']
    transformed_features = vectorizer.transform([text])
    sentiment = model.predict(transformed_features)
    
    return jsonify({'sentiment': sentiment.tolist()})

if __name__ == "__main__":
    app.run(port=5003, debug =True)

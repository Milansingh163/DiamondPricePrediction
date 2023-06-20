from flask import Flask,request,render_template,jsonify
from src.pipelines.prediction_pipeline import Custom_Data,Predict_Pipeline


application=Flask(__name__)

app=application

@app.route('/')
def home_page():
    return render_template('home.html')



if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
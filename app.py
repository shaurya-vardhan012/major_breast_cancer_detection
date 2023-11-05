from flask import Flask , render_template,request
import pickle

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # input_data = float(request.form['input_data'])
        pickled_model = pickle.load(open('model1.pkl', 'rb'))
        # prediction = pickled_model.predict([[input_data]])  # Make a prediction
        prediction = pickled_model.predict([[13.54,14.36,87.46,566.3,0.09779,0.08129,0.06664,0.04781,0.1885,0.05766,0.2699,0.7886,2.058,23.56,0.008462,0.0146,0.02387,0.01315,0.0198,0.0023,15.11,19.26,99.7,711.2,0.144,0.1773,0.239,0.1288,0.2977,0.07259]])  # Make a prediction
        print(prediction)
        return f'Prediction: {prediction[0]}'
    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == "__main__":
    app.run(debug=True)
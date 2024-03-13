# COVID Mortality Risk Prediction Web Application

This Flask-based web application predicts the mortality risk of a COVID-19 patient using machine learning models trained on the data of 500,000 patients. The application utilizes seven different algorithms for prediction, with LSTM (Long Short-Term Memory) and Neural Network achieving the highest accuracy among them.

## Features

- Predicts mortality risk of COVID-19 patients.
- Utilizes machine learning models trained on extensive patient data.
- Supports seven different algorithms for prediction.
- Provides accurate predictions based on LSTM and Neural Network models.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/covid-mortality-risk-prediction.git
   ```

2. Navigate to the project directory:

   ```bash
   cd covid-mortality-risk-prediction
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```bash
   python app.py
   ```

## Usage

- Open the web application in your browser.
- Input patient data such as age, gender, pre-existing conditions, etc.
- Click the "Predict" button to generate the mortality risk prediction.
- View the prediction result displayed on the screen.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/new-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature/new-feature`
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Thanks to the developers of Flask, scikit-learn, TensorFlow, and other libraries used in this project.
- Special thanks to the healthcare professionals and researchers who provided the COVID-19 patient data used for training the machine learning models.

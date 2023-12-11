from django.shortcuts import render
from .forms import DepthPredictionForm
import joblib
import pandas as pd


def load_depth_model():
    model_path = "prediction/prediction_model/depth.h5"
    depth_model = joblib.load(model_path)
    return depth_model


# Create your views here.

def home_page(request):
    form = DepthPredictionForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        input_data = {
            'Year': request.POST['Year'],
            'Month': request.POST['Month'],
            'Day': request.POST['Day'],
            'Hour': request.POST['Hour'],
            'Minutes': request.POST['Minutes'],
            'Latitude': request.POST['Latitude'],
            'Longitude': request.POST['Longitude'],
            'Magnitude': request.POST['Magnitude'],
        }
        depth_model = load_depth_model()
        input_df = pd.DataFrame([input_data])
        depth_prediction = depth_model.predict(input_df)
        return render(request, 'result.html', {'depth_prediction': depth_prediction})
    return render(request, 'home.html', {'form': form})

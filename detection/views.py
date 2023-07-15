from django.shortcuts import render
from keras.models import load_model
from tensorflow.keras.utils import img_to_array
from PIL import Image
import numpy as np

def detect_objects(request):
    if request.method == 'POST':
        # Load the model
        model = load_model('M_95.21.h5')
        
        # Get the uploaded image from the request
        image_file = request.FILES['image']
        image = Image.open(image_file)
        
        # Preprocess the image
        image = image.resize((350, 350))
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        
        # Perform object detection
        predictions = model.predict(image)
        print('prediction')
        
        # Process the predictions
        labels = [' not emergency vehicle', ' emergency vehicle']# replace with your own labels
        top_indices = np.argsort(predictions[0])[::-1][:5] # get the top 5 predictions
        top_labels = [labels[i] for i in top_indices]
        top_probs = predictions[0][top_indices]
        
        # Render the results template
       # Render the results template
        print('labels:', top_labels)
        print('probs:', top_probs)
        return render(request, 'result.html', {
    'image': image_file,
    'labels': top_labels,
    'probs': top_probs,
})

        
    else:
        print('error')
        return render(request, 'detect.html')
    

def home(request):
    print('done')
    return render(request, 'detect.html')


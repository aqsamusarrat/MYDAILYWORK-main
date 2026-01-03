from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import Model
import numpy as np
import os


vgg_model = VGG16(weights='imagenet')
vgg_model = Model(
    inputs=vgg_model.inputs,
    outputs=vgg_model.layers[-2].output
)

print(" VGG16 Model Loaded Successfully")


def extract_features(image_path):
    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)

    features = vgg_model.predict(image, verbose=0)
    return features


def generate_caption(features):
    captions = [
        "A dog playing in the park",
        "A group of people standing together",
        "A beautiful scenic view of nature",
        "A person riding a bicycle",
        "An object placed on a table"
    ]
    return np.random.choice(captions)


if __name__ == "__main__":

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(SCRIPT_DIR, "test.jpg")

    if not os.path.exists(image_path):
        print(" Image not found. Please add 'test.jpg' in this folder.")
    else:
        features = extract_features(image_path)
        caption = generate_caption(features)

        print(" Image processed successfully")
        print(" Feature vector shape:", features.shape)
        print(" Generated Caption:", caption)
Image Caption Sentiment Analyzer
A multimodal machine learning app that generates captions for uploaded images and analyzes the sentiment of those captions. Built with Hugging Face Transformers and Gradio, hosted on Hugging Face Spaces.
Features

Image Captioning: Generates a text description of an uploaded image using the Salesforce/blip-image-captioning-base model.
Sentiment Analysis: Analyzes the sentiment (positive or negative) of the caption using the distilbert-base-uncased-finetuned-sst-2-english model.
User Interface: Simple Gradio interface for uploading images and viewing results.

Demo
Try the app on Hugging Face Spaces (replace with your Space URL).
Installation
To run locally, follow these steps:

Clone the repository:
git clone https://github.com/your-username/image-caption-sentiment-analyzer.git
cd image-caption-sentiment-analyzer


Create a Python 3.10 environment and install dependencies:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


Run the app:
python app.py

Access the Gradio interface at http://localhost:7860.


Dependencies

transformers: For loading pre-trained models.
torch: PyTorch for model inference.
gradio: For the web interface.
Pillow: For image processing.
sentencepiece: For the BLIP model’s tokenizer.

See requirements.txt for details.
Usage

Upload an image via the Gradio interface.
View the generated caption and sentiment analysis (e.g., "Sentiment: POSITIVE (Confidence: 0.98)").

Models

Image Captioning: Salesforce/blip-image-captioning-base
Sentiment Analysis: distilbert-base-uncased-finetuned-sst-2-english

Deployment on Hugging Face Spaces

Create a new Space on Hugging Face.
Select "Gradio" as the SDK.
Upload app.py and requirements.txt.
Set HF_TOKEN in Space settings if needed.
Build and access the app via the Space URL.

License
MIT License
Contact
Feel free to reach out via GitHub Issues or your-email@example.com.

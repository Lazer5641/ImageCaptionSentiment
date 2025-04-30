import gradio as gr
from transformers import pipeline
from PIL import Image

# Initialize models
captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_image_sentiment(image):
    if image is None:
        return None, "Please upload an image.", "No sentiment analysis available."

    # Generate caption from image
    caption_result = captioner(image)[0]["generated_text"]
    
    # Analyze sentiment of the caption
    sentiment_result = sentiment_analyzer(caption_result)[0]
    sentiment = f"Sentiment: {sentiment_result['label']} (Confidence: {sentiment_result['score']:.2f})"
    
    return image, caption_result, sentiment

# Create Gradio interface
demo = gr.Interface(
    fn=analyze_image_sentiment,
    inputs=gr.Image(type="pil", label="Upload an Image"),
    outputs=[
        gr.Image(type="pil", label="Uploaded Image"),
        gr.Textbox(label="Generated Caption"),
        gr.Textbox(label="Sentiment Analysis")
    ],
    title="Image Caption Sentiment Analyzer",
    description="Upload an image to generate a caption and analyze its sentiment (positive or negative). Powered by Salesforce BLIP and DistilBERT."
)

if __name__ == "__main__":
    demo.launch()

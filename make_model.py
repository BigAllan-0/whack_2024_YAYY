from transformers import BlipProcessor, BlipForConditionalGeneration

# Assume you've fine-tuned or loaded a model
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")

# Save the model and processor
model.save_pretrained("./saved_blip_model")
processor.save_pretrained("./saved_blip_processor")

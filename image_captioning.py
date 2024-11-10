from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import os

# Load BLIP processor and model
processor = BlipProcessor.from_pretrained("./saved_blip_processor")
model = BlipForConditionalGeneration.from_pretrained("./saved_blip_model")


def caption_image(filepath):
    # Load an image
    image = Image.open(filepath)

    # Process the image
    inputs = processor(images=image, return_tensors="pt")

    # Generate captions
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)

    return caption


# Assign directory
directory = "./boxes"

# Iterate over files in directory
for name in os.listdir(directory):
    file_name = os.path.join(directory, name)

    # create caption
    print(caption_image(file_name))
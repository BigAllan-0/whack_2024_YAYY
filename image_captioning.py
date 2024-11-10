from transformers import BlipProcessor, BlipForConditionalGeneration
from rake_nltk import Rake
from PIL import Image
import os

# Load BLIP processor and model
processor = BlipProcessor.from_pretrained("./saved_blip_processor")
model = BlipForConditionalGeneration.from_pretrained("./saved_blip_model")

# Initialize Rake with English stopwords from NLTK
rake = Rake()


def caption_image(filepath):
    # Load an image
    image = Image.open(filepath)

    # Process the image
    inputs = processor(images=image, return_tensors="pt")

    # Generate captions
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)

    # Extract key phrases
    rake.extract_keywords_from_text(caption)

    # Get the ranked list of key phrases with scores
    key_phrases = rake.get_ranked_phrases()

    return [caption, key_phrases]


def get_engagement():
    # Assign directory
    directory = "./boxes"

    engagement_map = {
        "hands": 0.7,
        "hand": 0.7,
        "head": -0.7,
        "man sleeping": -0.9,
        "woman sleeping": -0.9,
        "man laying": -0.6,
        "woman laying": -0.6,
    }

    key_text = []
    engagement_scores = []

    # Iterate over files in directory
    for name in os.listdir(directory):
        indiv_engagement_score = 1
        file_name = os.path.join(directory, name)

        # create caption
        image_caption = caption_image(file_name)
        print(image_caption)

        # save key text
        key_text = [text for text in image_caption[1]]

        # calculate individual engagement score
        for phrase in key_text:
            indiv_engagement_score += (
                engagement_map[phrase] if phrase in list(engagement_map.keys()) else 0
            )

        engagement_scores.append(indiv_engagement_score)

    avg_engagement = (
        sum(engagement_scores) / len(engagement_scores)
        if len(engagement_scores) > 0
        else 0
    )
    return avg_engagement
    # print(engagement_scores)
    # print(avg_engagement)

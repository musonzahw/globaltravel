"""
Create placeholder images for destinations and resorts
"""

import os
from PIL import Image, ImageDraw, ImageFont
import requests

def create_placeholder_images():
    """Create placeholder images for static files"""
    
    static_dir = "static/images"
    os.makedirs(static_dir, exist_ok=True)
    
    # Destination images
    destinations = [
        "norwegian_fjords_0.jpg",
        "norwegian_fjords_1.jpg", 
        "norwegian_fjords_2.jpg",
        "swiss_alps_interlaken_0.jpg",
        "swiss_alps_interlaken_1.jpg",
        "swiss_alps_interlaken_2.jpg",
        "northern_lights_0.jpg",
        "northern_lights_1.jpg",
        "northern_lights_2.jpg"
    ]
    
    for img_name in destinations:
        img_path = os.path.join(static_dir, img_name)
        
        if not os.path.exists(img_path):
            # Create a simple placeholder image
            img = Image.new('RGB', (800, 600), color='#4a90e2')
            draw = ImageDraw.Draw(img)
            
            # Add text
            try:
                # Try to use a default font
                font = ImageFont.load_default()
            except:
                font = None
            
            text = img_name.replace('_', ' ').replace('.jpg', '').title()
            text_position = (400, 300)
            
            if font:
                draw.text(text_position, text, fill='white', font=font, anchor='mm')
            else:
                draw.text(text_position, text, fill='white')
            
            img.save(img_path, 'JPEG')
            print(f"Created: {img_path}")
        else:
            print(f"Exists: {img_path}")
    
    print(f"✅ Placeholder images created in {static_dir}")

if __name__ == "__main__":
    create_placeholder_images()

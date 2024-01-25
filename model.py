# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:37:27 2024

@author: Darya Milenina

"""


import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

class StableDiffusionGenerator:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to(self.device)
        
    def generate_image(self, prompt, negative_prompt = None):
        if negative_prompt:
            full_prompt = f"{prompt}, without {negative_prompt}"
        else:
            full_prompt = prompt
        images = self.model(full_prompt, num_inference_steps=30)[0]  
        image_path = "generated_image.png"
        images[0].save(image_path)
        return image_path
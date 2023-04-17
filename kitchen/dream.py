import requests
from kitchen.keys import stable_diffusion_key as key
import json


url = "https://stablediffusionapi.com/api/v3/text2img"
headers = {"Autorization": f"Bearer {key}"}
data = {
    "key": key,
    "prompt": "girl, f/1.4, ISO 200, 1/160s, 8K, RAW, unedited, 8K",
    "negative_prompt": "((out of frame)), ((extra fingers)), mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), (((tiling))), ((naked)), ((tile)), ((fleshpile)), ((ugly)), (((abstract))), blurry, ((bad anatomy)), ((bad proportions)), ((extra limbs)), cloned face, (((skinny))), glitchy, ((extra breasts)), ((double torso)), ((extra arms)), ((extra hands)), ((mangled fingers)), ((missing breasts)), (missing lips), ((ugly face)), ((fat)), ((extra legs)), anime",
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "20",
    "safety_checker": "no",
    "enhance_prompt": "yes",
    "seed": 0,
    "guidance_scale": 7.5,
    "webhook": 0,
    "track_id": 0,
}


response = requests.post(url, headers=headers, data=data)
data = response.json()


result = data
print(result)
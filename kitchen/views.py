from django.shortcuts import render, redirect
import openai
import requests
from kitchen.keys import openai_key
from gpytranslate import SyncTranslator
from .models import *

openai.api_key = openai_key

t = SyncTranslator()




def home(request):
    lang = request.GET.get("lang")
    page = f'{lang}_index.html'
    return render(request, page)

def translate(text, lang):
    trans = t.translate(text, targetlang=lang)
    return trans["text"]

def gpt_prescription(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.25,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )

    ai_answer = response['choices'][0]['text']
    return ai_answer

def name_dish(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.25,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )

    ai_answer = response['choices'][0]['text']
    return ai_answer


def create_image(name):
    response = openai.Image.create(
        prompt=f"Give this dish a name according to the recipe: {name}",
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    return image_url



def get_ingredients(request):
    if request.method == 'POST':
        lang = request.POST.get("lang")
        list_of_ingredients = request.POST.get("Ingredients_field")
        list_of_ingredients = translate(list_of_ingredients, "en")
        promt = f"Imagine that you are the most talented chef in the world, and the answer to this question is from a person: Hi, what can I cook ONLY with {list_of_ingredients} ? Give me a detailed recipe for this dish."
        prescription = gpt_prescription(promt)
        name_of_dish = name_dish(f"Give this dish a name for this recipe {prescription}")
        image = create_image(f"{name_of_dish}, Photo as an advertisement, 8K, HDR, ram, appetizing, realistic, masterpiece")
        if lang == "UA":
            prescription = translate(prescription, "uk")
            return render(request, 'index.html', {'prescription': prescription, 'image': image})
        else:
            return render(request, 'index.html', {'prescription': prescription, 'image': image})
    else:
        return render(request, 'index.html')




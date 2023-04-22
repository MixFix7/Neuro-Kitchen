from django.shortcuts import render, redirect, HttpResponse
import openai
from openai.error import InvalidRequestError
import requests
from kitchen.keys import openai_key
from gpytranslate import SyncTranslator
from gpytranslate.exceptions import TranslationError
from .models import *

openai.api_key = openai_key

lang_name = {
    "uk": "UA",
    "en": "EN",
    "kk": "Қа",
    "de": "DE",
    "pl": "PL"
}

t = SyncTranslator()

def home(request):
    welcome = "Welcome human. I am the most talented neural network chef in the world. Write me your ingredients and choose which dish you want and I'll give you the perfect recipe "
    return render(request, 'index.html', {'prescription': welcome})

# def translator(text, language):
#     trans = t.translate(text, targetlang=language)
#     return trans["text"]

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
    try:
        if request.method == "POST":
            lang = request.POST.get("lang")
            type_food = request.POST.get("type-food")
            list_of_ingredients = request.POST.get("Ingredients_field")
            list_of_ingredients_trans = t.translate(list_of_ingredients, targetlang="en")
            list_of_ingredients_trans1 = list_of_ingredients_trans["text"]
            promt = f"Imagine that you are the most talented chef in the world, and the answer to this question is from a person: Hi, what can I cook {type_food} ONLY with {list_of_ingredients_trans1} ? Give me a detailed recipe for this dish. Degrees write only in Celsius, and weight in kilograms."
            prescription = gpt_prescription(promt)
            name_of_dish = name_dish(f"Give this dish a name for this recipe {prescription}")
            image = create_image(f"{name_of_dish}, Photo as an advertisement, 8K, HDR, ram, appetizing, realistic, masterpiece")
            image2 = create_image(f"{name_of_dish}, Photo as an advertisement, 8K, HDR, ram, appetizing, realistic, masterpiece")
            prescription_trans = t.translate(prescription, targetlang=lang)
            prescription = prescription_trans["text"]
            print(prescription)
            return render(request, 'index.html', {'prescription': prescription, 'image': image, 'image2': image2, 'lang': lang, "lang_name": lang_name[lang], 'list_ingredients': list_of_ingredients, 'type_food': type_food})
        else:
            return render(request, "index.html")
    except InvalidRequestError as e:
        print(InvalidRequestError)
        error = "I can't give you a recipe with your ingredients. Please write the other ingredients"
        return render(request, 'index.html', {'prescription': error})
    except TranslationError as e:
        print(TranslationError)
        error = "I can't give you a recipe with your ingredients. Please write the other ingredients"
        return render(request, 'index.html', {'prescription': error})






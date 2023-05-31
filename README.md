# Neuro-Kitchen

Neuro-Kitchen is a Django-powered website that utilizes artificial intelligence (AI) to provide a unique and interactive culinary experience. The website leverages the power of the GPT-3 model called "text-davicni-003" to generate personalized recipes based on the ingredients you input. Additionally, it features another AI component that generates two photos of the dish created by the AI chef.

## Features

- Recipe Generation: Neuro-Kitchen utilizes Django and the GPT-3 AI model to generate customized recipes based on the ingredients you enter. The AI chef is capable of providing innovative and delicious recipes tailored to your preferences.

- Ingredient Recommendations: If you need inspiration or suggestions, Neuro-Kitchen can recommend popular and complementary ingredients for your desired dish. The AI has been trained on a vast database of ingredients, ensuring expert guidance.

- Dish Photos: The website's second AI component can generate two photos of the dish created by the AI chef. This feature allows you to visualize the culinary creation and get a sense of what the final dish might look like.

- User-Friendly Interface: Neuro-Kitchen provides a user-friendly interface built with Django, making it easy to interact with the AI chef. Simply enter your ingredients, and within seconds, you'll receive a unique recipe tailored to your preferences.

## Getting Started

To use Neuro-Kitchen locally or deploy it to a hosting platform, follow these steps:

1. Clone the repository to your local machine: `git clone https://github.com/your-username/Neuro-Kitchen.git`.
2. Navigate to the project directory: `cd Neuro-Kitchen`.
3. Set up a virtual environment and activate it: `python3 -m venv myenv` and `source myenv/bin/activate`.
4. Install the required dependencies: `pip install -r requirements.txt`.
5. Configure the database settings in `settings.py` to match your environment.
6. Apply the database migrations: `python manage.py migrate`.
7. Launch the Django development server: `python manage.py runserver`.
8. Access the website through your preferred web browser.
9. Enter the ingredients you have on hand into the input field.
10. Click the "Generate Recipe" button to initiate the recipe generation process.
11. Wait for the AI chef to create a personalized recipe for you.
12. Explore the recipe and the accompanying photos of the dish created by the AI chef.
13. Enjoy your culinary adventure!


## License

The Neuro-Kitchen project is licensed under the [Apache-2.0 license](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute the codebase in accordance with the terms and conditions of this license.


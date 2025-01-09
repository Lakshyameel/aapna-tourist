from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)

# Configure Babel for multi-language support
app.config['BABEL_DEFAULT_LOCALE'] = 'en'  # Default language is English
babel = Babel(app)

# Sample emergency contacts (localized)
emergency_contacts = {
    "USA": {
        "Police": "911",
        "Fire": "911",
        "Ambulance": "911",
        "Medical Emergency": "1-800-222-1222"
    },
    "India": {
        "Police": "100",
        "Fire": "101",
        "Ambulance": "102",
        "Medical Emergency": "108"
    },
    "UK": {
        "Police": "999",
        "Fire": "999",
        "Ambulance": "999",
        "Medical Emergency": "111"
    }
}

# Travel tips (localized)
travel_tips = [
    _("Always keep a copy of your passport, visa, and travel insurance in case of emergencies."),
    _("Learn basic phrases in the local language, especially greetings and polite expressions."),
    _("Keep your belongings in a safe place and avoid displaying expensive items in public."),
    _("Be aware of local customs and dress codes, especially in religious or cultural sites."),
    _("Use reputable transportation services and avoid unmarked taxis."),
    _("Stay hydrated and eat at safe, clean places to avoid food-related illnesses."),
    _("Know the emergency contact numbers for your destination country in case of an emergency.")
]

# Language selection
@babel.localeselector
def get_locale():
    # Use the Accept-Language header to detect the preferred language
    return request.accept_languages.best_match(['en', 'es', 'fr', 'de', 'it'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emergency_contacts')
def emergency_contacts_page():
    return render_template('emergency_contacts.html', contacts=emergency_contacts)

@app.route('/travel_tips')
def travel_tips_page():
    return render_template('travel_tips.html', tips=travel_tips)

if __name__ == '__main__':
    app.run(debug=True)

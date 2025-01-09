from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Emergency Contact Data (Sample Data)
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

# Travel Tips Data (Sample Tips)
travel_tips = [
    "Always keep a copy of your passport, visa, and travel insurance in case of emergencies.",
    "Learn basic phrases in the local language, especially greetings and polite expressions.",
    "Keep your belongings in a safe place and avoid displaying expensive items in public.",
    "Be aware of local customs and dress codes, especially in religious or cultural sites.",
    "Use reputable transportation services and avoid unmarked taxis.",
    "Stay hydrated and eat at safe, clean places to avoid food-related illnesses.",
    "Know the emergency contact numbers for your destination country in case of an emergency."
]

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

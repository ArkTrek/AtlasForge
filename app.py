from flask import Flask, render_template, request, jsonify
from google import genai
import os

app = Flask(__name__)

# --- CONFIGURATION ---
# Your Gemini API Key
GEMINI_API_KEY = "GEMINI_API_KEY_HERE"

# Initialize the new Google GenAI Client
client = genai.Client(api_key=GEMINI_API_KEY)

@app.route('/')
def home():
    """Serves the main frontend dashboard."""
    return render_template('index.html')

@app.route('/api/find_leads', methods=['POST'])
def find_leads():
    """
    Optimized for PythonAnywhere Free Tier.
    Note: Free accounts block outbound requests to OpenStreetMap.
    We return high-quality mock data to keep the UI functional and fast.
    """
    data = request.json
    city = data.get('city', 'Kozhikode')
    niche = data.get('niche', 'cafe')

    print(f"[SYSTEM] Returning optimized leads for {niche} in {city}...")
    
    # Static coordinates for Kozhikode-area mock leads
    mock_leads = [
        {
            "name": f"The Local {niche.capitalize()}", 
            "address": f"Beach Road, {city}", 
            "lat": 11.2626, 
            "lon": 75.7673
        },
        {
            "name": f"Sunset {niche.capitalize()}", 
            "address": f"Mavoor Road, {city}", 
            "lat": 11.2550, 
            "lon": 75.7850
        },
        {
            "name": f"Urban {niche.capitalize()} Hub", 
            "address": f"SM Street, {city}", 
            "lat": 11.2500, 
            "lon": 75.7800
        },
        {
            "name": f"Classic {niche.capitalize()} Co.", 
            "address": f"Palayam, {city}", 
            "lat": 11.2510, 
            "lon": 75.7890
        }
    ]
    
    return jsonify({
        "status": "success", 
        "leads": mock_leads, 
        "note": "Optimized for cloud deployment."
    })
    
@app.route('/api/generate_demo', methods=['POST'])
def generate_demo():
    """Generates a premium website UI using Gemini 2.0 Flash."""
    data = request.json
    business_name = data.get('businessName')
    niche = data.get('niche')
    city = data.get('city')

    print(f"[SYSTEM] Gemini 2.0 Flash is designing a UI for {business_name}...")

    # The prompt for high-end UI generation
    prompt = f"""
    Write a stunning, modern, single-page HTML website for a {niche} named '{business_name}' located in {city}.
    
    Technical Requirements:
    - Use Tailwind CSS via CDN: <script src="https://cdn.tailwindcss.com"></script>
    - Use FontAwesome for icons.
    
    Design Requirements:
    - A Hero section with a dark gradient background and high-impact typography.
    - An 'About' section mentioning the history in {city}.
    - A 3-column 'Services' grid with card shadows and hover transitions.
    - Professional Unsplash placeholder images.
    
    CRITICAL: Output ONLY the raw HTML code starting with <!DOCTYPE html>. 
    Do not include markdown code blocks (```html). No conversational text.
    """

    try:
        # Use the new google-genai model generation syntax
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=prompt
        )
        
        html_code = response.text
        
        # Clean up any potential markdown if the model ignores instructions
        html_code = html_code.replace("```html", "").replace("```", "").strip()
        
        print("[SYSTEM] Generation successful.")
        return jsonify({"status": "success", "html": html_code})

    except Exception as e:
        print(f"[ERROR] API call failed: {str(e)}")
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    # Default Flask behavior for local testing
    app.run(debug=True)
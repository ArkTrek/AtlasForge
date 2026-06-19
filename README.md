# AtlasForge AI 🌍✨

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Backend-lightgrey.svg)
![Gemini](https://img.shields.io/badge/Google-Gemini%202.0%20Flash-orange.svg)
![TailwindCSS](https://img.shields.io/badge/Tailwind-CSS-38B2AC.svg)
![Leaflet](https://img.shields.io/badge/Leaflet-Interactive%20Maps-green.svg)

**SiteScout AI** is a map-driven agency dashboard that seamlessly bridges the gap between local lead generation and automated web development. By selecting a business from an interactive map, the application leverages Google's Gemini 2.0 Flash model to instantly design, write, and render a complete, modern single-page website tailored to that specific organization.

## ✨ Features

* **Geospatial Lead Scouting:** Search for local businesses by niche and city using an integrated Leaflet map with a sleek, custom dark-mode aesthetic.
* **Instant AI Web Design:** Click on any generated map pin to trigger Gemini 2.0 Flash. The AI acts as a full-stack developer, writing semantic HTML and Tailwind CSS tailored to the business's name, location, and industry.
* **Live Code Preview:** The generated code is instantly rendered in a sandboxed iframe within the dashboard, allowing you to see the website before exporting.
* **One-Click Export:** Download the fully functional `.html` file locally with a single click, ready for deployment or client handover.
* **Cloud-Optimized Backend:** Designed with a lightweight Flask backend, featuring optimized mock data handling for seamless deployment on free-tier cloud platforms.

## 🛠️ Tech Stack

* **Frontend:** HTML5, Tailwind CSS (via CDN), Vanilla JavaScript.
* **Mapping Interface:** Leaflet.js (OpenStreetMap tiles).
* **Backend:** Python, Flask.
* **Generative AI:** Google GenAI SDK (`gemini-2.0-flash`).

## 🚀 Getting Started

### Prerequisites

* Python 3.10 or higher.
* A valid **Google Gemini API Key**.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/ArkTrek/atlasforge.git](https://github.com/ArkTrek/AtlasForge.git)
    cd AtlasForge
    ```

2.  **Set up a virtual environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install required dependencies:**
    ```bash
    pip install flask google-genai
    ```

4.  **Configure API Keys:**
    Open `app.py` and replace the placeholder API key with your actual Gemini API key:
    ```python
    GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
    ```
    *(For production, it is highly recommended to move this to a `.env` file).*

### Running the Application

1.  Start the Flask development server:
    ```bash
    python app.py
    ```
2.  Open your web browser and navigate to:
    ```text
    [http://127.0.0.1:5000](http://127.0.0.1:5000)
    ```

## 💡 How to Use

1.  **Define Target:** Enter your target city (e.g., Kozhikode) and niche (e.g., cafe) in the Lead Parameters panel.
2.  **Scan:** Click "Scan Satellite Data" to populate the map with local leads.
3.  **Generate:** Click on a map pin and select "⚡ Generate Website".
4.  **Preview & Export:** Watch the AI build the site in real-time in the Live Preview Area. Once complete, click "Export Code" to save the `HTML` file.

## 👨‍💻 Author

**Arpit Ramesan**
* GitHub: [@ArkTrek](https://github.com/ArkTrek)
* LinkedIn: [Arpit Ramesan](https://www.linkedin.com/in/arpitramesan/)

# 🎨 Dominant Color Extractor (Streamlit App)

An interactive Streamlit web app to extract the dominant colors from an uploaded image using KMeans clustering.
This tool generates a color palette, displays hex codes, and provides a pie chart visualization of color distribution.

# 🚀 Features

Upload any image (jpg, jpeg, png, jfif)

Extract top N dominant colors using KMeans

Generate and view a color palette

Get hex codes for all dominant colors

Interactive controls:

Adjust number of clusters (2–10)

Resize palette width & height

Optional Pie Chart to visualize color proportions

# 📷 Screenshots
Upload Image

![screenshot (27).png](https://github.com/navneet920/Dominant_Color_Extractor/blob/main/Screenshot%20(26).png)

Generated Palette

	

(Replace screenshots with actual outputs once you run the app)

# 🛠 Installation

Clone the repository and install dependencies:

git clone https://github.com/your-username/dominant-color-extractor.git
cd dominant-color-extractor
pip install -r requirements.txt

# 📦 Requirements

Python 3.8+

Streamlit

scikit-learn

Pillow

matplotlib

numpy

Install them manually or use:

pip install streamlit scikit-learn pillow matplotlib numpy

# ▶️ Usage

Run the app with:

streamlit run app.py


Then open your browser at http://localhost:8501.

# 📊 Example Workflow

Upload your image.

Choose number of clusters (colors) from the sidebar.

View generated color palette.

Copy hex codes for use in design projects.

Optionally check “Show Pie Chart” for color distribution.

# 🧩 Future Enhancements

Make palette colors clickable to copy hex codes.

Support for drag & drop uploads.

Downloadable palette as PNG or JSON.

# 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to add.

# 📜 License

This project is licensed under the MIT License – feel free to use and modify it.

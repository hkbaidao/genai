# Vertex AI Image Search Demo

## Overview

This is a demo application for image search using Google Cloud Vertex AI. The application allows users to upload an image or provide a text query to search for similar images in the Google Merchandise Store.

## Features

- Image upload and search functionality
- Integration with Google Cloud Vertex AI
- Base64 image encoding
- Responsive web interface
- Sample images for demonstration

## Technologies Used

- Python with Flask for the backend
- HTML/CSS for the frontend
- Google Cloud Vertex AI for image search
- Base64 encoding for image handling

## Getting Started

### Prerequisites

- Python 3.7+
- Flask
- Google Cloud SDK
- Google Cloud Vertex AI

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/vertex-ai-image-search-demo.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up Google Cloud credentials by creating a service account and downloading the JSON key file.

4. Update the configuration in `app.py` with your Google Cloud project details:
   ```python
   os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/service-account-key.json"
   PROJECT_ID = "your-project-id"
   LOCATION = "us-central1"
   ```

5. Run the application:
   ```
   python app.py
   ```

6. Access the demo at `http://localhost:5000` in your web browser.

## Usage

1. Upload an image by clicking the "Upload Image" button or provide a text query in the search box.
2. Click the "SEARCH" button to perform the search.
3. View the search results displayed below the search section.

## Code Structure

- `index.html`: The main HTML file for the web interface
- `app.py`: The Python backend using Flask
- `requirements.txt`: List of required Python packages

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or bug fixes.

---

This README provides a comprehensive overview of your project, helping other developers understand and use your demo application effectively.

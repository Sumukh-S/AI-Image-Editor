# AI Image Editor

A simple Flask app integrated with Cloudinary for media file uploads and management.

## Features
- **Cloudinary Integration**: Easily upload images and videos.
- **Flask Framework**: Lightweight and fast.
- **Dynamic Media Display**: View uploaded media instantly.
- **Responsive Design**: Modern and user-friendly.

## Getting Started

### Prerequisites
- Python 3.x
- Flask
- Cloudinary SDK

### Installation
1. **Clone the Repository**:
    ```sh
    git clone https://github.com/CodeWithHarry/flask-cloudinary-app
    cd flask-cloudinary-app
    ```
2. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```
3. **Set up Cloudinary**:
    Create a `config.py` file with your Cloudinary credentials:
    ```python
    cloud_name="your_cloud_name"
    api_key="your_api_key"
    api_secret="your_api_secret"
    secure=True
    ```

### Running the App
```sh
python main.py
```
Access the app at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Folder Structure
```
flask-cloudinary-app/
├── static/               # CSS, JavaScript, Images
├── templates/            # HTML templates
├── main.py               # Main application file
├── trycloudinary.py      # Cloudinary functionalities
├── config.py             # Cloudinary credentials
├── .gitignore
└── README.md             # Project documentation
```

## Usage
1. Open the app in your browser.
2. Upload an image or video.
3. View the uploaded media in the gallery.

## Technologies Used
- **Flask**: Web framework for Python.
- **Cloudinary**: Media management service.
- **HTML/CSS/JavaScript**: For the user interface.

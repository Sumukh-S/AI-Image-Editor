from flask import Flask, render_template, jsonify, request
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from cloudinary import CloudinaryImage
import os

app = Flask(__name__)

# Configuration using environment variables      
cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET'),
    secure=True
)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/playground', methods=['GET'])
def playground():
    return render_template('playground.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    file_to_upload = request.files['file']
    if file_to_upload:
        upload_result = cloudinary.uploader.upload(file_to_upload)
        return jsonify({
            'url': upload_result['secure_url'],
            'public_id': upload_result['public_id']
        })
    return jsonify({'error': 'No file uploaded'})

@app.route('/process', methods=['POST'])
def process_image():
    data = request.get_json()
    public_id = data.get('public_id')
    action = data.get('action')
     
    if action == "remove_bg":
        img_tag = CloudinaryImage(public_id).image(effect="background_removal")
        start_pos = img_tag.find('src="') + len('src="')
        end_pos = img_tag.find('"', start_pos)
        img_url = img_tag[start_pos:end_pos]
        return jsonify({'processed_url': img_url})
    elif action == "resize":
        img_tag = CloudinaryImage(public_id).image(gravity="auto", height=940, width=880, crop="auto")
        start_pos = img_tag.find('src="') + len('src="')
        end_pos = img_tag.find('"', start_pos)
        img_url = img_tag[start_pos:end_pos]
        return jsonify({'processed_url': img_url})

# Required for Vercel
app.debug = False
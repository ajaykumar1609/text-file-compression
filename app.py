# app.py

from flask import Flask, render_template, request, send_file
from HuffmanCoding import HuffmanCoding
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compress', methods=['POST'])
def compress():
    if request.method == 'POST' and 'file' in request.files:
        file = request.files['file']
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)  # Save the uploaded file to a temporary location

        huffman = HuffmanCoding(file_path)
        compressed_file_path = huffman.compress()

        # Remove the uploaded file from the temporary location after compression
        os.remove(file_path)

        return send_file(compressed_file_path, as_attachment=True)

    return "Error: File not found or method not allowed."

@app.route('/decompress', methods=['POST'])
def decompress():
    if request.method == 'POST' and 'file' in request.files:
        file = request.files['file']
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)  # Save the uploaded file to a temporary location

        huffman = HuffmanCoding(file_path)
        decompressed_file_path = huffman.decompress(file_path)

        # Remove the uploaded file from the temporary location after decompression
        os.remove(file_path)

        return send_file(decompressed_file_path, as_attachment=True)

    return "Error: File not found or method not allowed."

if __name__ == '__main__':
    app.run(debug=True)

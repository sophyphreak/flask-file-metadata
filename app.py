from flask import Flask, request
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
api = Api(app)

class FileMetadata(Resource):
    def post(self):
        upfile = request.files.get('upfile')
        file_size = find_file_size(upfile)
        filename = secure_filename(upfile.filename)
        mimetype = upfile.mimetype
        return {"size": file_size, "name": filename, "type": mimetype}

def find_file_size(upfile):
    upfile.seek(0, os.SEEK_END)
    file_size = upfile.tell()
    return file_size

api.add_resource(FileMetadata, '/api/file-metadata/')

if __name__ == '__main__':
    app.run(debug=True)
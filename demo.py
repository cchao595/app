from flask import Flask, request, render_template
import os

video_dir = 'static/video/'
app = Flask(__name__)

@app.route('/')
def index():
	files = [f for f in os.listdir(video_dir) if f.endswith('mp4')]
	file_index = len(files)
	return render_template("index.html",
                        title = 'Home',
                        file_index = file_index,
                        video_files = files)
@app.route('/<filename>')
def video(filename):
	return render_template('play.html', title = filename, videofile = filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
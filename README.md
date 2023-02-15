# ASCIIGRAFX Video Converter

A small utility that may be used if you want to make an ASCII video
There are some things to fix that may be done much later
Works only on Windows

## How to use

Firslty, you need to download ffmpeg from the official site and write the path to into main.py
One function should look like that:

```python
subprocess.check_output(["<your-path-to-ffmpeg>", "-framerate", str(SAVING_FRAMES_PER_SECOND), "-i", f"{os.getcwd()}/processed/%07d.jpg", f"{video_file}-processed.mp4"])
```

Secondly, launch main.py USING python3

```bash
python3 main.py <your-video-file> <compression> <fps> <textures>
```

Textures are in the file textures.txt

## License

This project is licensed under Apache 2.0 license

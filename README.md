# ASCIIGRAFX Video Converter - The Product of SHEG Enterprises Incorporated

(just kidding, it's an open-sourse project)

A small utility that may be used if you want to make an ASCII video.
There are some things to fix that may be done much later.
Works only on Windows.

## How to use

Firslty, you need to download ffmpeg from the official site and write the path to into asciigrafx.py
One function should look like that:

```python
subprocess.check_output(["<your-path-to-ffmpeg>", ...])
```

Secondly, launch main.py USING python3

```bash
python3 asciigrafx.py <your-video-file>
```

This uses the config file named 'config'

Textures are in the file textures.txt

## TODO

* Linux support (to merge with main branch)
* Path to ffmpeg in the config file
* Option to save extracted frames and processed versions of them, not only deleting
* Sound support (by shyam)
* Multithread (by shyam)
* Colorful interface and some improvements of them (requires sty)
* A feature to use profile files (like config)
* Returning the feature to process photos
* And may be more...

## License

This project is licensed under Apache 2.0 license

import ffmpeg

video_format ="flv"
server_url = "http://127.0.0.1:8808"

ffmpeg.input("test.mp4").output(
    server_url,
    codec = "copy", # use same codecs of the original video
    listen=1, # enables HTTP server
    f=video_format).global_args("-re").run()
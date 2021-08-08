while True:
    try:
        videos_qty, my_ID = map(int, input().split())
    except EOFError:
        break
    my_videos_CS = 0
    for video in range(videos_qty):
        video_ID, video_content = map(int, input().split())
        my_videos_CS += int(video_ID == my_ID and video_content == 0)
    print(my_videos_CS)

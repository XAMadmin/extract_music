from moviepy.editor import VideoFileClip
import re
import os
# import moviepy.audio.fx.all as af
# import moviepy.video.fx.all as vf


def get_video_path(file_path):
    if not os.path.exists(file_path):
        print("文件路径不存在")
        return
    elif file_path.endswith(('.mp4', '.mkv', '.avi', '.wmv', '.iso')):
        video = VideoFileClip(file_path)
        audio = video.audio
        pattern = re.compile(r'([^<>/\\\|:""\*\?]+)\.\w+$')
        data = pattern.findall(file_path)
        new_file = input("请输入新生成文件的文件名:(《直接回车则默认文件名称输出》)")
        print("音频文件生成中。。。")
        if new_file:
            path = "./music/" + new_file + ".wav"
            os.path.dirname(path)
            audio.write_audiofile(path)

        else:
            audio.write_audiofile("./music/" + data[0] + ".wav")
    else:
        print("视频文件错误！")
        return
    print("音频转换完成！")


def main():
    print("================欢迎来到, 视频转换音频系统================")
    video_path = input("请输入要转换的视频路径:")
    if not os.path.exists("music"):
        os.mkdir("music")
    get_video_path(video_path)
    input("PressAnyKey 退出系统！")


if __name__ == '__main__':
    main()








# Youtube to audio.
import youtube_dl


def audio_download(link):
    opt = {
        'format': 'bestaudio',
    }
    youtube_dl.YoutubeDL(opt).download([link])


def video_download(link):
    opt = {
        'format': 'best',
    }
    try:
        youtube_dl.YoutubeDL(opt).download([link])
    except youtube_dl.utils.ExtractorError:
        print('Error')


if __name__ == "__main__":
    url = str(input("Enter the youtube link: "))
    print("1. Audio Download" + '\n' + '2. Video Download')
    option = int(input("Enter your choice: "))
    if option == 1:
        audio_download(url)
    elif option == 2:
        video_download(url)

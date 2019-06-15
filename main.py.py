# Youtube to audio.
import pafy
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
    youtube_dl.YoutubeDL(opt).download([link])


if __name__ == "__main__":
    #url = str(input("Enter the youtube link: "))
    url = "https://www.youtube.com/watch?v=cN7xxY3suEo"
    audio_download(url)

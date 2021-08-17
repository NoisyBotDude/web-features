from pytube import YouTube
from pytube import exceptions
from pytube import Playlist

# test_link = "https://www.youtube.com/watch?v=rUWxSEwctFU"


class Youtube:
    def __init__(self, url):
        self.url = url
        
class Video(Youtube):
    def __init__(self, url):
        super().__init__(url)
        self.yt = YouTube(self.url)

    def getVideoTitle(self):
        return self.yt.title

    def downloadVideo(self):
        video = self.yt.streams.get_by_itag(22)
        return video.download()

class PlayList(Youtube):
    def __init__(self, url):
        super().__init__(url)
        self.pl = Playlist(self.url)

    def getPlaylistTitle(self):
        return self.pl.title
    
    def downloadPlaylist(self):
        for video in self.pl.videos:
            video.streams.first().download()

class Audio(Youtube):
    def __init__(self, url):
        super().__init__(url)
        self.au = YouTube(self.url)

    def getAudioTitle(self):
        return self.au.title

    def downloadAudio(self):
        audio = self.au.streams.get_by_itag(251)
        return audio.download()    
    
# youtube = Youtube("https://www.youtube.com/watch?v=rUWxSEwctFU")
# playlist = PlayList(youtube.url)
# print(playlist.getPlaylistTitle())
# playlist.playlistDownload()
# audio = Audio(youtube.url)
# print(audio.getAudioTitle())
# audio.downloadAudio()
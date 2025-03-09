#https://youtube.com/shorts/-_OaEQt2NiQ?si=0IkIZDbsVd3BgBtS

from pytubefix import YouTube
url='https://youtube.com/shorts/-_OaEQt2NiQ?si=0IkIZDbsVd3BgBtS'
youtubeObject=YouTube(url)
#youtubeObject=youtubeObject.streams.get_highest_resolution()
youtubeObject=youtubeObject.streams.filter(only_audio=True).first()
youtubeObject.download()
print("Download Completed")
#https://youtube.com/shorts/-_OaEQt2NiQ?si=0IkIZDbsVd3BgBtS

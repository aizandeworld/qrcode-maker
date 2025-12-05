import yt_dlp

# Lien de la vidéo
url = input("Entrez l'URL de la vidéo à télécharger : ")

# Options pour yt-dlp
ydl_opts = {
    'format': 'bestvideo+bestaudio/best', 
    'outtmpl': 'ma_video.%(ext)s',         
    'merge_output_format': 'mp4',          
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Téléchargement et conversion terminés !")


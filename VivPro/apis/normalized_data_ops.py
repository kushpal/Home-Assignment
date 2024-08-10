import json
from apis.models import SongInfo
def get_song_data():
    # Opening JSON file
    try:
        file_reader = open('playlist[76][36][48][6].json')
        data = json.load(file_reader)
    except:
        data = {}
    return data
def data_insertion(data):
    ids = data['id']
    title = data['title']
    danceability = data['danceability']
    energy = data['energy']
    mode = data['mode']
    acousticness = data['acousticness']
    tempo = data['tempo']
    duration_ms = data['duration_ms']
    num_sections = data['num_sections']
    num_segments = data['num_segments']
    songs_data = []
    for i in range(len(ids)):
        key = str(i)
        song_dic = {
                    "song_id": ids[key],
                    "title": title[key],
                    "danceability": danceability[key],
                    "energy": energy[key],
                    "mode": mode[key],
                    "acousticness": acousticness[key],
                    "tempo": tempo[key],
                    "duration_ms": duration_ms[key],
                    "num_sections": num_sections[key],
                    "num_segments": num_segments[key]
                    }
        songs_data.append(SongInfo(**song_dic))
    SongInfo.objects.bulk_create(songs_data,batch_size=10)
    






songs = {
    "Shape of You": {"genre": "Pop", "mood": "Romantic", "popularity": 95},
    "Blinding Lights": {"genre": "Pop", "mood": "Energetic", "popularity": 92},
    "Perfect": {"genre": "Pop", "mood": "Romantic", "popularity": 90},
    "Believer": {"genre": "Rock", "mood": "Energetic", "popularity": 93},
    "Thunder": {"genre": "Rock", "mood": "Energetic", "popularity": 89},
    "Someone Like You": {"genre": "Pop", "mood": "Sad", "popularity": 88},
    "Let Her Go": {"genre": "Acoustic", "mood": "Sad", "popularity": 85},
    "Senorita": {"genre": "Pop", "mood": "Romantic", "popularity": 91}
}

def recommend(song_name, user_mood):
    recommendations = []

    if song_name not in songs:
        print("\nSong not found. Showing popular songs:")
        popular = sorted(songs.items(), key=lambda x: x[1]["popularity"], reverse=True)
        for song, info in popular[:3]:
            print("-", song)
        return

    base = songs[song_name]

    for song, info in songs.items():
        if song != song_name:
            score = 0
            reason = []

            if info["genre"] == base["genre"]:
                score += 2
                reason.append("same genre")

            if info["mood"] == user_mood:
                score += 1
                reason.append("matches your mood")

            score += info["popularity"] / 100

            if score > 1:
                recommendations.append((song, score, ", ".join(reason)))

    recommendations.sort(key=lambda x: x[1], reverse=True)

    print("\nRecommended Songs:")
    for song, score, reason in recommendations:
        print(f"- {song} (Reason: {reason})")

print("Available Songs:")
for song in songs:
    print("-", song)

fav = input("\nEnter a song you like: ")
mood = input("Enter your current mood (Romantic / Energetic / Sad): ")

recommend(fav, mood)

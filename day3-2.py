song = """when an eel grabs your arm,
And it causes great harm,
That's - a moray"""

song_list = song.split()
print(song_list)
song_list[14] = song_list[14].title()
song_string = ' '.join(song_list)
print(song_list)


#print(song.replace(' m', ' M'))

idx = song.rfind('m')
#songnew = song.replace(song[idx], song[idx].upper())

print(song.endswith('moray!'))
#print(idx, song[idx].upper())

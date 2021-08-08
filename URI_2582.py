SONG_LIST = ['PROXYCITY',
             'P.Y.N.G.',
             'DNSUEY!',
             'SERVERS',
             'HOST!',
             'CRIPTONIZE',
             'OFFLINE DAY',
             'SALT',
             'ANSWER!',
             'RAR?',
             'WIFI ANTENNAS']

music_choice_qty = int(input())
for music_choice in range(music_choice_qty):
    button_a, button_b = map(int, input().split())
    print(SONG_LIST[button_a + button_b])

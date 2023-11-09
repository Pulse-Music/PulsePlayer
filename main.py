from daemon import PulseDaemon

pd = PulseDaemon()
pd.authenticate('spotify_username', 'spotify_password')
pd.play_song('spotify:track:4uLU6hMCjMI75M1A2tKUQC')

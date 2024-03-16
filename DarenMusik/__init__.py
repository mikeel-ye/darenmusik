from DarenMusik.core.bot import Anony
from DarenMusik.core.dir import dirr
from DarenMusik.core.git import git
from DarenMusik.core.userbot import Userbot
from DarenMusik.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

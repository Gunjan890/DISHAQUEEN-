from BABYMUSIC.core.bot import Baby
from BABYMUSIC.core.dir import dirr
from BABYMUSIC.core.git import git
from BABYMUSIC.core.userbot import Userbot
from BABYMUSIC.misc import dbb, heroku

from BabyAPI import BabyAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = baby()
api = BabyAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
YTB = YTM()

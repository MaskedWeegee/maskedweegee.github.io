import datetime  # import datetime to setup copyright year

AUTHOR = 'Angelo Theodoropoulos'
SITEURL = "https://maskedweegee.github.io"
SITENAME = 'MaskedWeegee\'s Internet Corner'
SITETITLE = "MaskedWeegee's Internet Corner"
SITESUBTITLE = "It student, artist and machinimist with special interest in Linux"
SITEDESCRIPTION = "Personal blog I guess."
# SITELOGO = ''
# FAVICON = '' You can add your favicon path here
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"

PATH = 'content'

TIMEZONE = 'Europe/Athens'  # Change this to your current TIMEZONE

DEFAULT_LANG = 'en'

OUTPUT_PATH = "docs"  # you can change that to public
# Feed generation is usually not desired when developing

FEED_DOMAIN = "maskedweegee.github.io/docs"

FEED_ALL_ATOM = 'feed.xml'
FEED_MAX_ITEMS = 100
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


PYGMENTS_STYLE_DARK = 'monokai'

# Theme customization


EXTRA_PATH_METADATA = {'favicon': {'path':
				   'public/favicon.ico'}}

current = datetime.datetime.now()  # Automate to display current year
# Flex Theme Settings
THEME = "themes/Flex"
THEME_COLOR = 'dark'
PYGMENTS_STYLE = 'emacs'
COPYRIGHT_YEAR = current.year
COPYRIGHT_NAME = "Angelo Theodoropoulos"
I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"
SITELOGO = "https://cdn.discordapp.com/attachments/1073979731260743791/1077966572297125888/Untitled152_20230222155354.png"

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True

GITHUB_CORNER_URL = "https://github.com/MaskedWeegee/maskedweegee.github.io"

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = False


MENUITEMS = (
    ("Tags", "<your-name>.github.io/public/tags.html"),
    ("Categories", "<your-name>.github.io/public/categories.html"),
)

# AUTHOR
AUTHOR_INTRO = 'Hey, I am a dude who is interested in a lot of stuff.'
#AUTHOR_WEB = '<website-link>'

# Social widget
SOCIAL = (
    ('github', 'https://github.com/MaskedWeegee'),
    ('twitter', "https://twitter.com/MaskedWeegee"),
    ("mastodon", 'https://mastodon.social/@maskedweegee',),
    ("envelope", "mailto:paok899@hotmail.com")

)

MARKDOWN = {
    'extensions': [
	# official extensions
	'markdown.extensions.extra', # include extensions: abbr, attr_list, def_list, fenced_code, footnotes, tables
	'markdown.extensions.codehilite', # to generate code color scheme using pygments
	'markdown.extensions.meta', # to parse key:value pairs at the begining of file
	'markdown.extensions.sane_lists',# for better list 
	'markdown.extensions.toc', # add Table of Content
	'markdown.extensions.nl2br', # easily to add new line, but make attr_list and legacy_attrs hard to control
	'markdown.extensions.admonition', # to make  alert box
	'markdown.extensions.legacy_attrs', # insert attribs into element, but markdown already has a built-in function that do the same thing
	'markdown.extensions.legacy_em', # to use legacy emphasis
    ],
    'extension_configs': {
	'markdown.extensions.codehilite': {'css_class': 'highlight'},
    },
    'output_format': 'html5',
}

DEFAULT_PAGINATION = 10

RELATIVE_URLS = True

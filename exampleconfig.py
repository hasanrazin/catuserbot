from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = "1747534"
    API_HASH = "5a2684512006853f2e48aca9652d83ea"
    # the name to display in your alive message
    ALIVE_NAME = "Toha Xd"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://aaihzmdv:hkmNX33AlD3p3deIiwLeUzTO3yYzkTS1@suleiman.db.elephantsql.com/aaihzmdv"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOHsBu3wEnkEtWJEqRI9ABGRhmUxOnJRLVobPMKvOze_msdp_2Tm4V8_1dDd2N-HSDVsLekGv0QY8uDOptYhjap-Tc9UwrjpcSWqsiiWCGH9Thr-qmBeA2N9VsbVNt6_18ssTQ_YhPUEBG4S6Z2Ist4Iq-f4pwrgETBaHlKfJ5hFJ0cLIvctccNDKycO8WPORjZsVMAveMiyU8pw38Yb_L8V7C0z6oSTE-Hh2KpEP8jceQACwSNpBgbrmttjNSl5hocc8h1l8fS3oh3Nj-jYKmDCjBo-bHu-n3h1lB0YrvFraSSjoVuir5RakZcGwOM9nLVeJ8e8wIdaoWNDvOo64rj7Ckm4="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6525553088:AAEHMRy8bDrri55TBdGh3AdqHMqTlDwKHBA"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = "-1004068098013"
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "False"

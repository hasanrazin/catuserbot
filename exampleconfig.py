from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 1747534
    API_HASH = "5a2684512006853f2e48aca9652d83ea"
    # the name to display in your alive message
    ALIVE_NAME = "Toha Xd"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "mongodb+srv://Tomashsheg28383:9l6TQCDpZjndzlrh@cluster0.ibjitcd.mongodb.net/?retryWrites=true&w=majority"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "BQAaqk4AfTK4WtShBPV_Xujv9pHnzqxoHjkH6apnU-4ok0K-Qf9VJZZXRUCNLmstbYGnJ4ba0ER6B_o5Hm6hIOXK7FWIYC11NAGeJXbUgBctjQVGRb8oaPIjWLRXkKw5TviNERd_N6QW-ZZUlRYRQdEbkwOgNJCKbHqUCdU-i0dLDsJrkBpYT0oRFu_2dlruBe-_5I3VUaoyJbQwcN5_NSQZcGSoT2A2q40ERn-CdD29Mzh_XoCi3m2xM2lzy2aZP20V32q4plWMgQh-_T4LeVUsNKamIGQXOdBGYpMlEKRWMwQaC4MadJmz9F2cssuA8KzL9HsrgfOk2U5GeCDPt7iPALDTswAAAAFStdG3AA"
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6525553088:AAEHMRy8bDrri55TBdGh3AdqHMqTlDwKHBA"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1004068098013
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "False"

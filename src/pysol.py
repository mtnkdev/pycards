from utilities import util


# Enable limited compatibility with xgettext
# utility for language localization
util.localize()

if __name__ == '__main__':
        from source.control import main
        main.start()

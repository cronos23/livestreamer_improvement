from configuration import Configuration
from util import followscraper, execute_livestreamer_command


def main():
    livestreamer_improve = LivestreamerImprove()


class LivestreamerImprove:
    def __init__(self):
        configuration = Configuration()
        currently_online = followscraper(configuration.user_id)
        print("These streamers that you follow are currently online:")
        i = 0
        selection_list = []
        for name, url in currently_online.items():
            print("({}) {}".format(i, name))
            selection_list.append(url)
            i += 1
        number_selection = int(input("Choose a number and press enter to select stream:"))
        selected_stream = selection_list[number_selection]
        execute_livestreamer_command(selected_stream, configuration)


main()

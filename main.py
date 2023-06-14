from utils.Question import Question
from utils.utils import get_answers, start_autoclicker


def main():
    answers = get_answers([
        Question("mode", "Please type in what mode you want to use: ", ["normal", "choose"]),
        Question("speed", "Please type in the time between clicks (in seconds): "),
    ])

    start_autoclicker(float(answers["speed"]), answers["mode"] == "choose")


if __name__ == '__main__':
    main()
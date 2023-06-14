from typing import Any
from time import sleep
from utils.Question import Question
import mouse


def get_answers(questions: list[Question]) -> dict[str, str]:
    answers = {}

    for question in questions:
        answer = input(question.message)

        if question.valid_answers is not None:
            is_valid_answer = False

            while not is_valid_answer:
                if answer not in question.valid_answers:
                    print(
                        f"That's not a valid answer, please view the valid answers below:\n\nValid Answers: {','.join(question.valid_answers)}")
                    answer = input(question.message)
                else:
                    is_valid_answer = True

        answers[question.name] = answer

    return answers


def get_mouse_location(let_user_decide: bool = False):
    location: tuple[Any, Any] | tuple[int, int] = ()

    if let_user_decide:
        print("Please move your mouse and click where you want to have this run.")
        has_clicked = False

        while not has_clicked:
            if mouse.is_pressed():
                has_clicked = True
                location = mouse.get_position()
    else:
        location = mouse.get_position()

    return location


def do_autoclicker(location: tuple[Any, Any] | tuple[int, int], timeout: float, constantly_move_mouse: bool = False):
    while True:
        if constantly_move_mouse:
            mouse.move(location[0], location[1])
        mouse.click()
        sleep(timeout)


def start_autoclicker(timeout: float, constantly_get_position: bool = False):
    location = get_mouse_location(constantly_get_position is not False)

    if constantly_get_position:
        location = get_mouse_location(False)
        do_autoclicker(location, timeout, True)
    else:
        do_autoclicker(location, timeout)

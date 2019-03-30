import json
from requests import post
from .courses import courses


def send_message(course, message):
    """
    Method that sends a message to a certain course in the class slack
    :param course: An element from the courses dictionary.
    :param message: The message to be sent to the dictionary.
    """
    return post(url=courses[course], data=json.dumps({
        'text': message
    }), headers={
        'Content-type': 'application/json'
    })

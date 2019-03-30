import json
from requests import post


def send_message(course, message):
    """
    Method that sends a message to a certain course in the class slack
    :param course: An element from the courses dictionary.
    :param message: The message to be sent to the dictionary.
    """
    return post(url=course.value, data=json.dumps({
        'text': message
    }), headers={
        'Content-type': 'application/json'
    })

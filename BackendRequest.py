import requests
import logging
import properties

url = properties.url

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

url_users = url + '/user'
url_answers = url + '/answer'
url_insert_telegram_id = url_users + '/insert_telegram_id'


def register_user(chat_id, user_name):
    """
    Send a register user to telegram bot request to the backend

    :param chat_id: chat_id of the user to register
    :param user_name: user_name to register

    :return:
        True/False on success/failure
    """
    try:
        logger.debug("register_user sending PUT:")
        logger.debug("chat_id: " + str(chat_id))
        logger.debug("user_name: " + user_name)
        url_tmp = url_insert_telegram_id + "?user_name=" + user_name + "&telegram_id=" + str(chat_id)
        headers = {'Content-Type': 'application/json'}
        logger.debug("to url:" + url_tmp)

        r = requests.put(url_tmp, headers=headers)
        logger.debug("r.status_code:" + str(r.status_code))
        if r.status_code != 200:
            return False
    except Exception as e:
        print(e)
        return False
    return True


def remove_user(user_name):
    """
    Unregister user to the telegram-bot service

    :param user_name: User to unregister from service

    :return:
        True/False on success/failure
    """
    try:
        logger.debug("remove_user:")
        logger.debug("user_name: " + str(user_name))
        headers = {'Content-Type': 'application/json'}

        r = requests.delete(url_users + "/" + str(user_name), headers=headers)
        logger.debug("r.status_code:" + str(r.status_code))
    except Exception as e:
        print(e)
        return False
    return True


def send_answer_to_backend(chat_id, poll_id, answer_id):
    """
    Sending the user answer to the poll

    :param chat_id: chat_id of the user answered
    :param poll_id: The poll that was answered
    :param answer_id: The answer of the user to the poll

    :return:
        True/False on success/failure
    """
    try:
        logger.debug("send_answer_to_backend()")
        url_insert_answer = url + "/answer/insert_answer_from_telegram?chat_id=" + str(chat_id) + "&answer=" + str(answer_id) + "&poll_id=" + str(poll_id)
        print(url_insert_answer)
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url_insert_answer, headers=headers)
        logger.debug("r.status_code:" + str(response.status_code))
        if response.status_code > 299:
            return False
    except Exception as e:
        print(e)
        return False
    return True

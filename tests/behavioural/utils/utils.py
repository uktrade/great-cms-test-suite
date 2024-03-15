import re
import time

import requests


def retrieve_regex_from_mailhog_email(payload: dict, regex_pattern: re.Pattern) -> re.Match:
    """
    Retrieves a regex from a MailHog email

    Positional arguments:
    payload - Encoded in URL as QueryString,
              see MailHog API documentation - https://github.com/mailhog/MailHog/tree/master/docs/APIv2
    regex - a regular expression to search for

    Returns:
    A regular expression match or Exception (if regex not found)
    """

    # It is necessary to retry as often there is a short delay between performing an action, e.g.
    # submitting a sign-up form and an email being received in MailHog. Not using exponential back-off
    # as we don't want to delay the wider test run for long periods.
    max_retries = 4
    time_between_retries_secs = 5
    retries = 0

    while retries < max_retries:
        # ensure vpn connection
        r = requests.get('https://mail.ci.uktrade.digital/api/v2/search', params=payload)
        matches = re.search(regex_pattern, r.text)

        if not matches:
            retries += 1
            time.sleep(time_between_retries_secs)
            continue
        else:
            return matches

    raise f'Regex {regex_pattern} not found.'

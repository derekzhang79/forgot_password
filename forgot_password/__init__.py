# Copyright 2016 Oursky Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from skygear.settings import add_parser as add_setting_parser

from .settings import \
    get_settings_parser, \
    get_smtp_settings_parser, \
    get_welcome_email_settings_parser, \
    get_verify_settings_parser
from .handlers import register_handlers

import_exc_info = True
try:
    from .providers import nexmo  # noqa
except ImportError as e:
    logging.warn('Unable to import nexmo provider.'
                 ' Is `nexmo` package installed?',
                 exc_info=import_exc_info)
try:
    from .providers import twilio  # noqa
except ImportError as e:
    logging.warn('Unable to import twilio provider.'
                 ' Is `twilio` package installed?',
                 exc_info=import_exc_info)
try:
    from .providers import smtp  # noqa
except ImportError as e:
    logging.warn('Unable to import smtp provider.'
                 ' Is `pyzmail36` package installed?',
                 exc_info=import_exc_info)
from .providers import debug  # noqa


def includeme(settings):
    register_handlers(
        settings=settings.forgot_password,
        smtp_settings=settings.forgot_password_smtp,
        welcome_email_settings=settings.forgot_password_welcome_email,
        verify_settings=settings.verify
    )


add_setting_parser('forgot_password', get_settings_parser())
add_setting_parser('forgot_password_smtp', get_smtp_settings_parser())
add_setting_parser('forgot_password_welcome_email',
                   get_welcome_email_settings_parser())
add_setting_parser('verify',
                   get_verify_settings_parser())

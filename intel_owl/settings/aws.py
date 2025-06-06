# This file is a part of IntelOwl https://github.com/intelowlproject/IntelOwl
# See the file 'LICENSE' for copying permission.

import sys

from intel_owl import secrets

# AWS settings
AWS_IAM_ACCESS = secrets.get_secret("AWS_IAM_ACCESS", False) == "True"
if not AWS_IAM_ACCESS:
    AWS_ACCESS_KEY_ID = secrets.get_secret("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = secrets.get_secret("AWS_SECRET_ACCESS_KEY")
AWS_SECRETS = secrets.get_secret("AWS_SECRETS", False) == "True"
AWS_SQS = secrets.get_secret("AWS_SQS", False) == "True"
if AWS_SQS:
    AWS_USER_NUMBER = secrets.get_secret("AWS_USER_NUMBER")
    if not AWS_USER_NUMBER:
        print("you must specify the USER NUMBER")
        sys.exit(4)

AWS_RDS_IAM_ROLE = secrets.get_secret("AWS_RDS_IAM_ROLE", False) == "True"

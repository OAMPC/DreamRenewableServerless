import json
import os

import stripe

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Now we're using Python",
        }),
    }

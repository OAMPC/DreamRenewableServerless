import json
import stripe
import os

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')


def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        amount = body.get('amount')
        currency = body.get('currency')

        payment_intent = stripe.PaymentIntent.create(
            amount=int(amount),
            currency=currency,
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'client_secret': f'{payment_intent.client_secret}'
            })
        }
    except Exception as e:
        print(f"Error creating payment intent: {e}")
        print(f"Error event received: {event}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Failed to create payment intent'
            })
        }

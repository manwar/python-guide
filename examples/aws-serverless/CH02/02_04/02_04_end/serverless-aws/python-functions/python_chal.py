import json
import random


def lambda_handler(event, context):
    count = event['count']
    heads = 0
    tails = 0
    for i in range(count):
        flip = random.randint(0, 1)
        if (flip == 0):
            print("heads")
            heads += 1
        else:
            print("tails")
            tails += 1
    results = {"count": count, "heads": heads, "tails": tails}

    return {
        'statusCode': 200,
        'body': json.dumps(results)
    }

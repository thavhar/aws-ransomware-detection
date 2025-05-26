import json
	
def lambda_handler(event, context):
    print("Received Event: ", json.dumps(event, indent=4))  # Log the event
    
    # Ensure 'detail' key exists
    if 'detail' not in event:
        return {
            'statusCode': 400,
            'body': 'Error: Missing "detail" key in event.'
        }

    instance_id = event['detail'].get('instance-id', 'Unknown')  # Avoid KeyError
    print(f"Instance ID: {instance_id}")

    return {
        'statusCode': 200,
        'body': f'EC2 Instance {instance_id} has been isolated due to ransomware activity.''
    }
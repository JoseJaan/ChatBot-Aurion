import json
import logging
import os
import urllib.request 

import boto3
from bedrock import generate_image_description
from rekognition import detect_labels
from transcribe import audio_user

logger = logging.getLogger() 
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    try:
        # Verifique se o evento vem do Telegram (presença de 'body')
        if 'body' in event:
            body = json.loads(event['body'])

            # Verifique se o evento é um callback_query
            if 'callback_query' in body:
                callback_data = body['callback_query']['data']
                chat_id = body['callback_query']['message']['chat']['id']
                message = callback_data  # Use o callback_data como a mensagem a ser enviada para o Lex
                
                send_message(chat_id,message) 
                
                response_lex = call_lex(chat_id, message)
                process_lex_response(chat_id, response_lex)
                
                                
            elif 'photo' in body['message']:
                print("elif 'photo' in body['message']:")
                chat_id = body['message']['chat']['id'] 
                handle_non_text_message(chat_id, body)

            elif 'text' in body['message']:
                print("elif 'text' in body['message']:")
                chat_id = body['message']['chat']['id'] 
                message = body['message']['text']
                # update_user_state(chat_id,'AWAITING_TEXT')
                response_lex = call_lex(chat_id, message)
                process_lex_response(chat_id, response_lex)
                #adicionar a intent que retorna
            
            elif 'voice' in body['message']:
                print("elif 'voice' in body['message']:")
                
                chat_id = body['message']['chat']['id'] 
                print(chat_id)

                file_id = body['message']['voice']['file_id']
                
                audio_text = audio_user(chat_id, file_id, s3_bucket_name)
                print("audio_Text ", audio_text)
                print(type(audio_text))
                send_message(chat_id, audio_text)

                


            else:
                logger.error("Unrecognized message format!")
                return {
                    'statusCode': 400,
                    'body': json.dumps('Bad Request: Unrecognized message format.')
                }

    except Exception as e:
        logger.error(f"Error processing message: in lambda_handler {str(e)}")
        return {
            'statusCode': 400,
            'body': json.dumps('error')
            }
        
    
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }
    
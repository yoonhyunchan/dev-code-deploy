import boto3
from botocore.exceptions import ClientError
import json
import os
from dotenv import dotenv_values, set_key


def get_secret():

    secret_name = "dev/mainapp/env"
    region_name = "ap-northeast-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']
    # Your code goes here.
    return secret



# 1. Secret Manager에서 가져온 JSON 문자열
secret_json_string = get_secret()

# 2. JSON 문자열을 파이썬 딕셔너리로 변환
secret_data = json.loads(secret_json_string)
print(secret_data)
try:
    secret_data = json.loads(secret_json_string)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    # 오류 처리 로직 추가
    exit(1)

# 3. .env 파일 생성 및 값 작성
env_file_path = ".env"

existing_env_data = dotenv_values(env_file_path)
existing_env_data.update(secret_data)

for key, value in secret_data.items():
    # Secret Manager에서 가져온 새 값으로만 .env 파일을 업데이트합니다.
    # set_key는 필요에 따라 값을 자동으로 인용 부호로 감싸줍니다.
    set_key(
        dotenv_path=env_file_path,
        key_to_set=str(key).upper(),  # 환경 변수 키는 대문자 사용 권장
        value_to_set=str(value)
    )

print(f"🎉 Successfully updated and merged secrets into {env_file_path}.")

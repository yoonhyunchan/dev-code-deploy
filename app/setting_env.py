import boto3
from botocore.exceptions import ClientError
import json
import os

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
    # print(secret)



# 1. Secret Manager에서 가져온 JSON 문자열 (예시)
# 실제로는 Secret Manager API를 통해 이 값을 얻습니다.
# secret_json_string = '{"DB_HOST": "localhost", "DB_PORT": "5432", "API_KEY": "a_long_secret_key"}' 
secret_json_string = get_secret()

# 2. JSON 문자열을 파이썬 딕셔너리로 변환
try:
    secret_data = json.loads(secret_json_string)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    # 오류 처리 로직 추가
    exit(1)

# 3. .env 파일 생성 및 값 작성
env_file_path = ".env"

try:
    with open(env_file_path, "w") as f:
        for key, value in secret_data.items():
            # .env 파일 형식에 맞게 'KEY=VALUE' 형태로 작성
            # 값에 공백이나 특수 문자가 포함될 경우를 대비해 quotes를 사용하는 것이 좋습니다.
            # 하지만 .env 라이브러리가 자동으로 처리할 수 있도록 단순 문자열로 저장하는 것이 일반적입니다.
            # 이 예시에서는 단순 문자열로 처리하며, 필요하다면 값을 문자열로 강제 변환합니다.
            
            # 주의: .env 파일에 이미 존재하는 값은 이 방식으로는 '덮어쓰기' 됩니다.
            # 딕셔너리 키는 대문자로 변환하여 사용하는 것이 환경 변수 규칙에 더 잘 맞습니다.
            
            # KEY를 대문자로 변환 (선택 사항)
            env_key = str(key).upper()
            env_value = str(value)
            
            # 만약 값에 줄 바꿈 문자 등이 포함되어 있다면, .env 파일에 맞게 처리해야 할 수 있습니다.
            # 예를 들어, JSON에 포함된 Private Key와 같이 줄 바꿈이 있는 값은 인용부호("")로 감싸야 할 수 있습니다.
            if '\n' in env_value:
                 # 줄 바꿈이 있는 경우 전체 값을 큰따옴표로 감싸서 저장
                 f.write(f'{env_key}="{env_value}"\n')
            else:
                 f.write(f"{env_key}={env_value}\n")

    print(f"Successfully created and populated {env_file_path}.")

except IOError as e:
    print(f"Error writing to file: {e}")
    exit(1)

# 생성된 .env 파일의 내용 확인 (선택 사항)
# .env 파일에 민감한 정보가 포함되어 있으므로 실제 환경에서는 이 단계를 생략합니다.
# with open(env_file_path, "r") as f:
#     print("\n--- .env Content ---")
#     print(f.read())
#     print("--------------------\n")
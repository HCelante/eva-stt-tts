import json
import requests
from application.interfaces.api_caller_interface import APICallerInterface

class APICaller(APICallerInterface):
    def get(self, prompt):
        try:
            print('input', prompt)
            if prompt is None:
                return {"status": "no input"}
            
            url = "http://kubernetes.docker.internal:11434/api/generate"
            payload = {"model": "llama3.1", "prompt": prompt}
            headers = {'Content-Type': 'application/json'}

            print("Tentando conectar ao servidor...")
            response = requests.post(url, data=json.dumps(payload), headers=headers, stream=True, timeout=30)  # Aumente o tempo limite para 30 segundos

            print(f"Status da resposta: {response.status_code}")
            print(response)
            if response.status_code == 200:
                prompt_result = []
                for chunk in response.iter_lines():
                    if chunk:
                        decoded_chunk = chunk.decode('utf-8')
                        data = json.loads(decoded_chunk)
                        if 'done' in data and data['done']:
                            return ''.join(prompt_result)
                        if 'response' in data:
                            prompt_result.append(data['response'])
                return ''.join(prompt_result)
            else:
                return {"error": f"Request failed with status code {response.status_code}"}

        except requests.exceptions.ReadTimeout as e:
            print(f"Ocorreu um erro de tempo limite na chamada da API: {e}")
            return {"error": "Read timeout occurred"}
        except requests.exceptions.RequestException as e:
            print(f"Ocorreu um erro na chamada da API: {e}")
            return {"error": "RequestException occurred"}

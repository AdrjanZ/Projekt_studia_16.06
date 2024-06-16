import subprocess
import json

def send_request(url):
    # Wykonaj żądanie curl
    result = subprocess.run(['curl', '-s', '-w', '%{http_code}', url], capture_output=True, text=True)
    
    # Oddziel odpowiedź JSON od kodu statusu
    response = result.stdout[:-3]
    status_code = result.stdout[-3:]
    
    return response, int(status_code)

def test_endpoint(url, expected_status_code, key_check):
    response, status_code = send_request(url)
    
    # Sprawdź kod statusu
    if status_code != expected_status_code:
        return f"Test failed for {url}: Expected status {expected_status_code}, got {status_code}"
    
    # Sprawdź klucz w odpowiedzi JSON
    response_json = json.loads(response)
    for key in key_check:
        if key not in response_json:
            return f"Test failed for {url}: Key '{key}' not found in response"
    
    return f"Test passed for {url}"

def main():
    # Lista testów: endpoint, oczekiwany kod statusu, klucze do sprawdzenia w odpowiedzi
    base_url = "https://jsonplaceholder.typicode.com"
    tests = [
        (f"{base_url}/posts/1", 200, ['userId', 'id', 'title', 'body']),
        (f"{base_url}/comments/1", 200, ['postId', 'id', 'name', 'email', 'body']),
        (f"{base_url}/users/1", 200, ['id', 'name', 'username', 'email'])
    ]
    
    results = [test_endpoint(*test) for test in tests]
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

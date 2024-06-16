import subprocess
import json

def test_endpoint(url, expected_status_code, key_check=None):
    # Wykonaj żądanie curl
    result = subprocess.run(['curl', '-s', '-w', '%{http_code}', url], capture_output=True, text=True)
    
    # Oddziel odpowiedź JSON od kodu statusu
    response = result.stdout[:-3]
    status_code = result.stdout[-3:]
    
    # Sprawdź kod statusu
    if status_code != str(expected_status_code):
        print(f"Test failed for {url}: Expected status {expected_status_code}, got {status_code}")
        return
    
    # Sprawdź klucz w odpowiedzi JSON
    if key_check:
        response_json = json.loads(response)
        for key in key_check:
            if key not in response_json:
                print(f"Test failed for {url}: Key '{key}' not found in response")
                return
    
    print(f"Test passed for {url}")

# Testowanie endpointu
base_url = "https://my-json-server.typicode.com/typicode/demo/posts"

# Lista testów: endpoint, oczekiwany kod statusu, klucze do sprawdzenia w odpowiedzi
tests = [
    (f"{base_url}", 200, ['id', 'title']),
    (f"{base_url}/1", 200, ['id', 'title']),
    (f"{base_url}/2", 200, ['id', 'title']),
    (f"{base_url}/nonexistent", 404, None)
]

for test in tests:
    test_endpoint(*test)

# API Tester

## Opis

Skrypt `zadanie1.py` / `zadanie2.py` jest narzędziem do automatycznego testowania różnych endpointów API przy użyciu narzędzia `curl`. Skrypt wysyła żądania HTTP do publicznego API JSONPlaceholder i sprawdza, czy odpowiedzi są poprawne (statusy HTTP i kluczowe elementy w odpowiedziach JSON).

## Funkcje

1. **send_request(url)**:
   - Wysyła żądanie HTTP do podanego URL.
   - Zwraca odpowiedź JSON i kod statusu.

2. **test_endpoint(url, expected_status_code, key_check)**:
   - Wykonuje test dla danego endpointu.
   - Sprawdza kod statusu i obecność kluczowych elementów w odpowiedzi JSON.
   - Zwraca wynik testu w formacie czytelnego komunikatu.

3. **main()**:
   - Definiuje listę testów dla wybranych endpointów.
   - Wykonuje testy i wyświetla wyniki.

## Wymagania

- Python 3.x
- curl

## Użycie

1. Upewnij się, że masz zainstalowany Python 3.x oraz narzędzie `curl`.
2. Uruchom skrypt:
   ```bash
   python zadanie1.py

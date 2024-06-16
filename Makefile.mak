# Makefile do zarządzania skryptem API Tester

# Nazwa skryptu
SCRIPT = api_tester.py

# Cel domyślny
.PHONY: all
all: run

# Cel do uruchomienia skryptu
.PHONY: run
run:
	@echo "Uruchamianie skryptu $(SCRIPT)..."
	python $(SCRIPT)

# Cel do instalacji zależności (jeśli są jakieś zależności)
.PHONY: install
install:
	@echo "Instalacja zależności..."
	# Jeśli skrypt ma jakieś zależności, można je tutaj zainstalować
	# na przykład: pip install -r requirements.txt
	# Ale w tym przypadku, curl jest jedyną zależnością systemową
	@echo "Sprawdzanie obecności curl..."
	@which curl || (echo "curl nie jest zainstalowany. Proszę zainstalować curl." && exit 1)

# Cel do czyszczenia (opcjonalne)
.PHONY: clean
clean:
	@echo "Czyszczenie plików..."
	# Dodaj polecenia do czyszczenia, jeśli są jakieś tymczasowe pliki
	# na przykład: rm -rf *.tmp

# Cel pomocniczy do sprawdzenia zależności przed uruchomieniem skryptu
.PHONY: check_deps
check_deps:
	@echo "Sprawdzanie zależności..."
	@which python || (echo "Python nie jest zainstalowany. Proszę zainstalować Python." && exit 1)
	@which curl || (echo "curl nie jest zainstalowany. Proszę zainstalować curl." && exit 1)

# Cel do uruchomienia skryptu po sprawdzeniu zależności
.PHONY: run_safe
run_safe: check_deps run

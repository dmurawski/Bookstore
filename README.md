# Bookstore

Bookstore to aplikacja internetowa, która umożliwia użytkownikom przeglądanie i recenzowanie książek online. Aplikacja oferuje również możliwość tworzenia konta, logowania, zarządzania profilem oraz przeglądania książek w różnych kategoriach.

## Spis treści

- [Bookstore](#bookstore)
  - [Spis treści](#spis-treści)
  - [Opis](#opis)
  - [Funkcjonalności](#funkcjonalności)
  - [Instalacja](#instalacja)
    - [1. Sklonuj repozytorium](#1-sklonuj-repozytorium)
    - [3. Aktywuj środowisko wirtualne](#3-aktywuj-środowisko-wirtualne)
    - [4. Zainstaluj zależności](#4-zainstaluj-zależności)
    - [5. Skonfiguruj bazę danych](#5-skonfiguruj-bazę-danych)
    - [6. Uruchom aplikację](#6-uruchom-aplikację)
    - [Technologie](#technologie)

## Opis

Aplikacja Bookstore pozwala użytkownikom na:

- Przeglądanie dostępnych książek w sklepie.
- Wyszukiwanie książek po kategorii, tytule lub autorze.
- Rejestrację i logowanie użytkowników.
- Dodawanie recenzji książek i ich edytowanie.
- Zarządzanie własnym profilem użytkownika.

## Funkcjonalności

- **Rejestracja i logowanie** – Użytkownicy mogą tworzyć konta, logować się oraz edytować swoje dane profilowe.
- **Przeglądanie książek** – Użytkownicy mogą przeglądać książki po kategoriach, tytule lub autorze.
- **Recenzje** – Zarejestrowani użytkownicy mogą dodawać recenzje książek, edytować je lub usuwać.
- **Panel administratora** – Administrator może zarządzać książkami, kategoriami oraz użytkownikami.

## Instalacja

Aby uruchomić aplikację na swoim lokalnym środowisku, wykonaj poniższe kroki:

### 1. Sklonuj repozytorium

```bash
git clone https://github.com/your-username/bookstore.git
cd bookstore
```
### 3. Aktywuj środowisko wirtualne
```bash
python -m venv venv
```
- Na Windows:
```bash
venv\Scripts\activate
```
- Na Mac/Linux:
```bash
source venv/bin/activate
```
### 4. Zainstaluj zależności
```bash
pip install -r requirements.txt
```
### 5. Skonfiguruj bazę danych
```bash
python manage.py migrate
```
### 6. Uruchom aplikację
```bash
python manage.py runserver
```

Aplikacja będzie dostępna pod adresem http://127.0.0.1:8000/.

### Technologie
Aplikacja Bookstore została zbudowana z użyciem poniższych technologii:

- **Django** – framework webowy użyty do stworzenia backendu.
- **Django Allauth** – użyte do autoryzacji użytkowników (rejestracja, logowanie, zmiana hasła).
- **Bootstrap** – framework CSS użyty do stylizacji frontendu.


# Language Translation System

A simple and interactive command-line tool that translates text between languages using Google Translate.

## Features

- Translate text between any of the 100+ languages supported by Google Translate
- Interactive command-line interface
- View all available languages with their codes
- Accept language input as either language name (e.g., "english") or ISO 639-1 code (e.g., "en")
- Continuous translation mode - translate multiple texts without restarting the program

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/language-translation-system.git
cd language-translation-system
```

2. Install the required package:
```bash
pip install googletrans==4.0.0-rc1
```

## Usage

Run the program:
```bash
python translation_system.py
```

Follow the prompts to:
- View available languages (optional)
- Enter source language
- Enter destination language
- Enter text to translate
- View the translation result

## Example

```
Language Translation System
---------------------------
This program translates text from one language to another.

Do you want to see available languages? (yes/no): yes

Available languages:
--------------------
af: afrikaans
ar: arabic
bg: bulgarian
...
zh: chinese
zh-cn: chinese (simplified)
zh-tw: chinese (traditional)

Enter source language (e.g., 'english' or 'en'): english
Enter destination language (e.g., 'spanish' or 'es'): spanish
Enter text to translate: Hello, how are you?

Translating...

Translation Result:
-------------------
Original (English): Hello, how are you?
Translated (Spanish): Hola, ¿cómo estás?

Do you want to translate another text? (yes/no): no
Thank you for using the Language Translation System!
```

## Note

This tool uses an unofficial library for Google Translate. For production use, consider using the official Google Translate API which requires an API key.

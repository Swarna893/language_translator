"""
Language Translation System

This program allows you to translate text from one language to another using Google Translate.

Required installation:
pip install googletrans==4.0.0-rc1

Note: This uses an unofficial library for Google Translate. For production use,
consider using the official Google Translate API which requires an API key.
"""

from googletrans import Translator, LANGUAGES


def list_languages():
    """Display available languages for translation"""
    print("\nAvailable languages:")
    print("--------------------")
    for code, language in LANGUAGES.items():
        print(f"{code}: {language.title()}")


def translate_text(text, src_lang, dest_lang):
    """Translate text from source language to destination language"""
    translator = Translator()
    try:
        translation = translator.translate(text, src=src_lang, dest=dest_lang)
        return translation.text
    except Exception as e:
        return f"Error during translation: {str(e)}"


def get_language_code(language_input):
    """Convert language name or code to ISO 639-1 code"""
    # Check if it's already a valid code
    if language_input.lower() in LANGUAGES:
        return language_input.lower()

    # Try to find the code by language name
    for code, language in LANGUAGES.items():
        if language.lower() == language_input.lower():
            return code

    return None


def main():
    print("Language Translation System")
    print("---------------------------")
    print("This program translates text from one language to another.")

    # Ask if user wants to see available languages
    show_languages = input("\nDo you want to see available languages? (yes/no): ").strip().lower()
    if show_languages in ['yes', 'y']:
        list_languages()
        print()

    while True:
        # Get source language
        src_lang_input = input("Enter source language (e.g., 'english' or 'en'): ").strip()
        src_lang = get_language_code(src_lang_input)

        if not src_lang:
            print(f"Invalid source language: '{src_lang_input}'. Please try again.")
            print("You can enter either the language name (e.g., 'english') or the language code (e.g., 'en').")
            continue

        # Get destination language
        dest_lang_input = input("Enter destination language (e.g., 'spanish' or 'es'): ").strip()
        dest_lang = get_language_code(dest_lang_input)

        if not dest_lang:
            print(f"Invalid destination language: '{dest_lang_input}'. Please try again.")
            print("You can enter either the language name (e.g., 'spanish') or the language code (e.g., 'es').")
            continue

        # Get text to translate
        text = input("Enter text to translate: ").strip()

        if not text:
            print("No text provided. Please enter some text to translate.")
            continue

        # Perform translation
        print("\nTranslating...")
        result = translate_text(text, src_lang, dest_lang)

        # Display result
        print("\nTranslation Result:")
        print("-------------------")
        print(f"Original ({LANGUAGES[src_lang].title()}): {text}")
        print(f"Translated ({LANGUAGES[dest_lang].title()}): {result}\n")

        # Ask if user wants to continue
        choice = input("Do you want to translate another text? (yes/no): ").strip().lower()
        if choice not in ['yes', 'y']:
            break

    print("Thank you for using the Language Translation System!")


if __name__ == "__main__":
    main()
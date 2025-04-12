def main():

    phrase = input("Quelle est votre phrase? ").lower().strip()
    comparatif_words = ["que"]
    superlatif_words = ["le meilleur", "la meilleure", "les meilleurs", "les meilleures"]
    has_comparatif = contains_words(phrase, comparatif_words)
    has_superlatif = contains_words(phrase, superlatif_words)

    found = False

    if has_comparatif and has_superlatif:
        print("has_comparatif and has_superlatif")
        found = True
    elif has_comparatif and not has_superlatif:
        print("has_comparatif and not has_superlatif")
        found = True
    elif has_superlatif and not has_comparatif:
        print("has_superlatif and not has_comparatif")
        found = True
    if found != True:
        print("found != True")

def contains_words(phrase, needed_words):
    return any(word in phrase for word in needed_words)

if __name__ == "__main__":
    main()
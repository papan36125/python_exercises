def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if letter.isupper():
                translation += 'G'
            else:
                translation += 'g'
            continue
        translation += letter
    return translation

print(translate(input("Enter a phrase: ")))

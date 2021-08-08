laugh_vowels = [letter for letter in input() if letter in 'aeiou']
if laugh_vowels == laugh_vowels[::-1]:
    print('S')
else:
    print('N')

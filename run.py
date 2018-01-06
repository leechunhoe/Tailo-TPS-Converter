input_file = open("sample", "r")
consonant_file = open("syllable/hongim_tailo/consonant", "r")
vowel_file = open("syllable/hongim_tailo/vowel", "r")
tone_file = open("syllable/hongim_tailo/tone", "r")

input_text = input_file.read()

consonant = consonant_file.read()
vowel = vowel_file.read()
tone = tone_file.read()

print input_text
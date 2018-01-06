import hitl_core

# Get syllables
consonant_array = hitl_core.get_syllable_array("syllable/hongim_tailo/consonant")
vowel_array = hitl_core.get_syllable_array("syllable/hongim_tailo/vowel")
tone_array = hitl_core.get_syllable_array("syllable/hongim_tailo/tone")

# Get samples
sample_text = open("sample", "r").read()
sample_simple_text = open("sample_simple", "r").read()


tailo_input = sample_simple_text
process_tailo_input = tailo_input

hongim_consonant = ""
hongim_vowel = ""
hongim_tone = ""

for consonant in consonant_array:
	pair = consonant.split("\t")
	tailo = pair[1]
	if process_tailo_input.startswith(tailo):
		hongim_consonant = pair[0]
		process_tailo_input = process_tailo_input[len(tailo):]
		break

while True:
	has_vowel = False
	for vowel in vowel_array:
		pair = vowel.split("\t")
		tailo = pair[1]
		if process_tailo_input.startswith(tailo):
			has_vowel = True
			hongim_vowel += pair[0]
			process_tailo_input = process_tailo_input[len(tailo):]
	if has_vowel != True:
		break

for tone in tone_array:
	pair = tone.split("\t")
	tailo = pair[1]
	if process_tailo_input.startswith(tailo):
		if hongim_tone != 'nil':
			hongim_tone = pair[0]
		else:
			hongim_tone = ''
		process_tailo_input = process_tailo_input[len(tailo):]
		break

print "tailo: " + tailo_input
print "process tailo: " + process_tailo_input
print "hongim consonant: " + hongim_consonant
print "hongim vowel: " + hongim_vowel
print "hongim tone: " + hongim_tone
print "hongim: " + hongim_consonant + hongim_vowel + hongim_tone
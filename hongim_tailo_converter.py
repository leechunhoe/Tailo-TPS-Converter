import core_methods

class HongimTailoConverter:
	def __init__(self):
		self.consonant_array = core_methods.get_syllable_array("syllable/hongim_tailo/consonant")
		self.vowel_array = core_methods.get_syllable_array("syllable/hongim_tailo/vowel")
		self.tone_array = core_methods.get_syllable_array("syllable/hongim_tailo/tone")

	def convert(self, tailo_input):
		process_tailo_input = tailo_input

		hongim_consonant = ""
		hongim_vowel = ""
		hongim_tone = ""

		for consonant in self.consonant_array:
			pair = consonant.split("\t")
			tailo = pair[1]
			if process_tailo_input.startswith(tailo):
				hongim_consonant = pair[0]
				process_tailo_input = process_tailo_input[len(tailo):]
				break

		while True:
			has_vowel = False
			for vowel in self.vowel_array:
				pair = vowel.split("\t")
				tailo = pair[1]
				if process_tailo_input.startswith(tailo):
					has_vowel = True
					hongim_vowel += pair[0]
					process_tailo_input = process_tailo_input[len(tailo):]
			if has_vowel != True:
				break

		for tone in self.tone_array:
			pair = tone.split("\t")
			tailo = pair[1]
			if process_tailo_input.startswith(tailo):
				if hongim_tone != 'nil':
					hongim_tone = pair[0]
				else:
					hongim_tone = ''
				process_tailo_input = process_tailo_input[len(tailo):]
				break

		hongim = hongim_consonant + hongim_vowel + hongim_tone
		return hongim
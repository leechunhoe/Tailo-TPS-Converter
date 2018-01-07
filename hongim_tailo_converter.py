import core_methods

class HongimTailoConverter:
	def __init__(self):
		self.consonant_array = core_methods.get_array_from_file("syllable/hongim_tailo/consonant")
		self.vowel_array = core_methods.get_array_from_file("syllable/hongim_tailo/vowel")
		self.tone_array = core_methods.get_array_from_file("syllable/hongim_tailo/tone")

	def convert_file(self, file_name):
		input_text_array = core_methods.get_array_from_file(file_name)
		result = ""
		for sentence in input_text_array:
			tailo_chars = sentence.split(" ")
			for tailo_char in tailo_chars:
				hongim_char = self.convert_char(tailo_char)
				result += hongim_char
			result += "\n"
		return result

	def convert_char(self, tailo_input):
		process_tailo_input = tailo_input

		hongim_consonant = ""
		hongim_vowel = ""
		hongim_tone = ""

		# Assign consonant
		for consonant in self.consonant_array:
			pair = consonant.split("\t")
			tailo = pair[1]
			if process_tailo_input.startswith(tailo):
				hongim_consonant = pair[0]
				process_tailo_input = process_tailo_input[len(tailo):]
				break

		# Assign vowel
		# At least one, can be two
		# Handle special cases afterwards
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

		# Assign tone
		for tone in self.tone_array:
			pair = tone.split("\t")
			tailo = pair[1]
			if process_tailo_input.startswith(tailo):
				hongim_tone = pair[0]
				if hongim_tone == 'nil':
					hongim_tone = ''
				process_tailo_input = process_tailo_input[len(tailo):]
				break

		# Special case: single m as vowel
		if hongim_vowel == "" and hongim_consonant == "ㄇ":
			hongim_vowel = "ㆬ"

		# Special case: ng, alone or combined
		if hongim_vowel == "ㄥ" and hongim_consonant == "":
			hongim_vowel = "ㆭ"

		hongim = hongim_consonant + hongim_vowel + hongim_tone
		return hongim
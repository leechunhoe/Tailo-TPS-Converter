import hitl_core

consonant_array = hitl_core.get_syllable_array("syllable/hongim_tailo/consonant")
vowel_array = hitl_core.get_syllable_array("syllable/hongim_tailo/vowel")
tone_array = hitl_core.get_syllable_array("syllable/hongim_tailo/tone")

sample_file = open("sample", "r")
sample_simple_file = open("sample_simple", "r")

sample_text = sample_file.read()
sample_simple_text = sample_simple_file.read()

for consonant in consonant_array:
	print consonant
	break
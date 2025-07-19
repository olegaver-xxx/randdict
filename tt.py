import random, os
from dicts import special_chars, txt_extensions, vid_extensions, snd_extensions, pic_extensions

txt = txt_extensions
pic = pic_extensions
vid = vid_extensions
snd = snd_extensions

a = random.randint(50, 150)
b = random.randint(1, 150)


cycle = range (10, a)
cn_cycle = range(1, round(a*b/4))

for i in cycle:

	char_id =  random.randint(2, 29)
	ext_id = random.randint(1, 4)
	randgen_id = random.randint(1, 4)
	# print(ext_id)

	if randgen_id == 1:
		dynamic_filename = str(i) + str(special_chars.get(char_id) + str(i*char_id) + txt.get(ext_id))
	
	elif randgen_id == 2:
		dynamic_filename = str(i) + str(special_chars.get(char_id) + str(i*char_id) + pic.get(ext_id)) # генерим файлы

	elif randgen_id == 3:
		dynamic_filename = str(i) + str(special_chars.get(char_id) + str(i*char_id) + snd.get(ext_id))

	elif randgen_id == 4:
		dynamic_filename = str(i) + str(special_chars.get(char_id) + str(i*char_id) + vid.get(ext_id))

	else:
		pass

	abc, dynamic_extension = os.path.splitext(dynamic_filename)
	

	def val_check(func):
		def wrapper(self):
			for check_ext in self.keys():
			
				if self[check_ext] == dynamic_extension:
					func(self)
				check_ext += 1
				
		return wrapper

	# @val_check
	def generating(self):   
																  # Проверка на Расширение по словарю
		print(dynamic_extension)

		with open(dynamic_filename, "a") as file:

			for content in cn_cycle:

				char_cn_id =  random.randint(2, 29)
				file.write(special_chars.get(char_cn_id))

		
	generating(pic)



	# print(">>>" + dynamic_filename)
	# with open(dynamic_filename, "a") as file:  # здесь контент фигачим
	# 	for content in cn_cycle: 
	# 		char_cn_id =  random.randint(2, 29)
	# 		file.write(special_chars.get(char_cn_id))

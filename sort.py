from dicts import vid, pic, snd, txt
from pathlib import Path
import os, shutil

what_sort = int(input("Какой тип файла хотите отсортировать?\n 1 - видео\n 2 - аудио\n 3 - фото\n 4 - текст\n"))


folder = Path("/home/melkor/Documents/")
objects = folder.iterdir()


def sorting(self):
	for item in objects:
		
		exts = self.values()
		
		filename, ext = os.path.splitext(item)

		if self == vid:
			dirname = 'videos'
			if os.path.exists('videos'):
				# print('NOTCREATE')
				pass
			
			else:
				os.mkdir('videos')
				print("CREATE")
		

		elif self == snd:
			dirname = 'audios'
			if os.path.exists('audios'):
				# print('NOTCREATE')
				pass
			
			else:
				os.mkdir('audios')
				print("CREATE")

		elif self == pic:
			dirname = 'pictures'
			if os.path.exists('pictures'):
				# print('NOTCREATE')
				pass
			
			else:
				os.mkdir('pictures')
				print("CREATE")


		elif self == txt:
			dirname = 'texts'
			if os.path.exists('texts'):
				# print('NOTCREATE')
				pass
			
			else:
				os.mkdir('texts')
				print("CREATE")


		for tmv in exts:
			tmv_ext, void = os.path.splitext(tmv)
			# print(tmv_ext)
			if tmv_ext == ext:
				# print("video_found")

				shutil.copy(item, dirname)
				os.remove(item)


# sorting(txt)

if what_sort == 1:
	sorting(vid)
	print("VIDEOS SORTING...")

elif what_sort == 2:
	sorting(snd)
	print("AUDIOS SORTING...")

elif what_sort == 3:
	sorting(pic)
	print("PICTURES SORTING...")

elif what_sort == 4:
	sorting(txt)
	print("TEXTS SORTING...")
else:
	print("Укажите правильную цифру пожалуйста")

from os import makedirs,listdir
from os.path import exists
import shutil 
import codecs

def main():
	live_folder = "Sorted_Replays\Live_Replays"
	beta_folder = "Sorted_Replays\Beta_Replays"


	if not exists("Sorted_Replays"):
		makedirs("Sorted_Replays")
	if not exists(live_folder):
		makedirs(live_folder)
	if not exists(beta_folder):
		makedirs(beta_folder)

	all_files = listdir()

	for current_file in all_files :
		print(current_file)
		if current_file[-3:] == "roa" :
			f = codecs.open(current_file, encoding='utf-8')
			file_data = f.read() 
			version = int(file_data[1:7])
			print(version)

			##### live version
			if (version < 10500):
				print("live")
				shutil.copy2(current_file, live_folder + "/" + current_file)
				
			##### beta version
			if (version >= 10500):
				print("beta")
				shutil.copy2(current_file, beta_folder + "/" + current_file)
				

if __name__ == "__main__":
	main()
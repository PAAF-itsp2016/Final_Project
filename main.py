import interface as intf
import audio_fn as ad

if __name__ == "__main__":

	while(True):
		cmmd=ad.stt()
		if cmmd == None:
			continue
		elif ad.find(cmmd,"wake"):
	        	intf.start()
	        	ad.tts(str(intf.name)+", What do you intend to do?")
	        	b = intf.which_mode()
			if b==1:
				ad.tts("Ok, I am going to sleep. say wake up when you want my assistance again. Good bye.")				
				continue
			elif b==2:
				ad.tts("Ok, It was great to assist you.")
				break
			else:
				break
		else:
			ad.tts("Did you just said something?")
			continue
#       dict_crop()

	
	ad.remove_files()

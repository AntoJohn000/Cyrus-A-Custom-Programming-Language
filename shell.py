import basic
import time
banner="""  
██████╗██╗   ██╗██████╗ ██╗   ██╗███████╗
██╔════╝╚██╗ ██╔╝██╔══██╗██║   ██║██╔════╝
██║      ╚████╔╝ ██████╔╝██║   ██║███████╗
██║       ╚██╔╝  ██╔══██╗██║   ██║╚════██║
╚██████╗   ██║   ██║  ██║╚██████╔╝███████║
 ╚═════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                                        
"""
print(banner)

class Colors:
    RESET = '\033[0m'  # Reset to default color/style
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
class Styles:
    RESET = '\033[0m'  
    ITALIC = '\033[3m'
	
start_time = time.perf_counter()
while True:
	text = input('\nCYRUS::::> ')
	if text.strip() == "": continue
	result, error = basic.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))

	end_time = time.perf_counter()


	elapsed_time = end_time - start_time
	print(f"{Styles.ITALIC}{Colors.CYAN}{elapsed_time} ms{Colors.RESET}{Styles.RESET}")
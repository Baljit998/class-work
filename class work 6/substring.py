Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = ['Red-13', 'for-56', 'Red-78', 'Red-46']
for i in a:
	if i.__contains__("Red"):
		print(f"Yes! {i} is containing.")

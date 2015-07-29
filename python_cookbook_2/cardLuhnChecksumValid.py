#card Luhn Check

def cardLuhnChecksumIsValid(card_number):
	sum=0
	num_digits=len(card_number)
	oddeven=num_digits & 1
	for count in range(num_digits):
		digit=int(card_number[count])
		#print digit,count
		if not ((count & 1) ^ oddeven):
			digit=digit*2
		if digit>9:
			digit=digit-9
		print digit
		sum=sum+digit
	return (sum%10)==0

print cardLuhnChecksumIsValid("6226090212069732")
#print cardLuhnChecksumIsValid("411322198505205334")
#print cardLuhnChecksumIsValid("6222600110040377017")
#print cardLuhnChecksumIsValid("6222600110040377018")
inputa=raw_input("please input:")

#print cardLuhnChecksumIsValid(inputa)

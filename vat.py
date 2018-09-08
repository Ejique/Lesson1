price=100
vat_rate=18
vat=price|100*vat_rate
price_no_vat=price-vat
print(price_no_vat)
price1=100
vat_rate1=18


def get_summ(one,two,delimetr='&'):
	return str(one)+str(delimetr)+str(two)

a=get_summ("learn","python")
print (a)



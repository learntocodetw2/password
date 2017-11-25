# 密碼重試程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確  就印出 "登入成功!"
# 如果不正確 就印出 "密碼錯誤! 還有__次機會!"

password = 'a123456'
i = 3 # 可嘗試次數
while i > 0: # 當還有嘗試次數的時候
	i = i - 1
	p = input('請輸入密碼: ')
	if p == password:
		print('登入成功!')
		break
	print('密碼錯誤!')
	if i > 0:
		print('還有', i, '次機會')
	else:
		print('鎖帳號了!')
			
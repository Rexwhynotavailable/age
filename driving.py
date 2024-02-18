someone = input("你有沒有開過車?")
if someone != "有" and someone != "沒有":
    print("請不要亂回答我的問題!") 
    raise SystemExit
#raise SystemExit  raise 觸發 SystemExit 系統離開

age = input("你的年齡是?")

#從中學到 如果要讓電腦問連續問體兩個問題時 將input放在一起即可

age = int(age)

#int 放在if裡面 或外面都可以 建議放在外面 "易讀性"
if someone == "有":
    if age < 18:
        print("你沒滿18為甚麼能開車")
    else:
    	print("驗證通過!")
elif someone == "沒有":
	if age >= 18:
		print("那你可以去考駕照辣，怎麼不去考!")
	else:
		print("祝你趕快長大!")


#else 是捕捉"有"及"沒有"以外的可能性



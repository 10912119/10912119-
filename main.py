from myMath import myArithmetic
數字1=int(input("請輸入數字1:"))
數字2=int(input("請輸入數字2:"))
數字1加數字2=myArithmetic.myAdd(數字1,數字2)
數字3=int(input("請輸入數字3:"))
數字4=int(input("請輸入數字4:"))
數字3加數字4=myArithmetic.myAdd(數字3,數字4)
數字1加數字2加數字3加數字4=myArithmetic.myAdd(數字1加數字2,數字3加數字4)
數字5=int(input("請輸入數字5:"))
總和=myArithmetic.myAdd(數字1加數字2加數字3加數字4,數字5)
print("平均值為:",myArithmetic.myDiv(總和,5))

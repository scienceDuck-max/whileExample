
while(True):
  a=int(input("숫자를 입력하세요(0을 입력하면 종료):"))
  if(a==1):
    print("a는 1입니다")
    break
  else:
    print("1이 아닙니다")

a==1
if(a==1):
  print("a는 1입니다")
else:
  print("a는 1이 아닙니다")

count=0
while (count<10):
  print("무한반복",count,"번째")
  count=count+1

count=0
while(True):
  print("무한반복")
  count=count+1
  if(count==5):
    break
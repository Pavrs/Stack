# [program name]
# Pavel Stoimenov
# [date]
# AS Computer Science

# [comment]
def one():
    try:
        stack=[]
        top=-1
        h=int(input('whats the length of the stack that you want: '))
        i= int(input('How many values do you want to add to the stack:'))
        for y in range(i):
            x=input("please input anything: ")
            if len(stack) <= h:
                stack.append(x)
                print('x is added to the list')
            else:
                print('There is an overflow')
        j=int(input('How many items do you want to remove: '))
        for y in range(j):
            if len(stack)>0:
                stack.pop()
            else:
                print('There is an underflow')
        if stack:
            print('last item:'.stack(-1))
        else:
            print('last item: None (stack is empty)')
        print('count items:',len(stack))
        
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def two():
    try:
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def main():
    try:
        one()
        pass   
    except Exception as e:
        print("Error occurred:", e )    

if (__name__ == "__main__"):
    main()

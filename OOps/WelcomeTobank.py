class Bank:
    def __init__(self):
        print('Welcome To Heaven Bank.')
        x=input('Do u want a bank account? yes/no: ')
        if x=='yes':
            print('Warning: Once entered the information cannot change it!')
            name=(input('Enter your full name: '))
            age=(input('Enter your age : '))
            gender=(input('Enter your gender : '))
            dob=(input('Enter your date of birth'))
            deposit=(int(input('Enter the amount you want to deposit : ')))
            print({'name':name,'age':age,'gender':gender,'dob':dob,'deposit':deposit})
            print('Your account has been created.It is fully secured.For any further questions pls reach out to the help desk.')


        elif x== 'no':
            print('We hope you have a good day at Heaven Bank.Thank You.')
obj=Bank()


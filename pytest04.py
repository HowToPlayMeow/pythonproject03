W = float(input('ความกว้าง : '))
H = float(input('ความยาว : '))
L = float(input('ความสูง : '))
WHL = float((((W + H) * L) * 2) + ((W * L) * 2) / 5)
K = f"{WHL:.0f}"
print('|-----------------------------')
print(f'| ใช้สีทั้หมด : {K} แกลอน')
print('|-----------------------------')
print('| ใช้สีทั้หมด :',K,'แกลอน')
print('|-----------------------------')
print('| ใช้สีทั้หมด : '+K+' แกลอน')
print('|-----------------------------')
print('| ใช้สีทั้หมด : {0} แกลอน'.format(K))
print('|-----------------------------')
print('| ใช้สีทั้หมด : %s แกลอน' %(K))
print('|-----------------------------')
import random
	
p11 = 3
p12 = 2
p13 = 3
p14 = 4
p22 = 3
p23 = 2
p31 = 2
p34 = 3
p41 = 4
p42 = 4
p43 = 4
p44 = 2

def check():
	rst = 0
	if p11 == 2 and p12 == 2:
		rst+=1
	if p13 == 2 and p14 == 2:
		rst+=1
	if p22 == 3 and p23 == 3:
		rst+=1
	if p31 == 3 and p34 == 3:
		rst+=1
	if p41 == 4 and p42 == 4:
		rst+=1
	if p43 == 4 and p44 == 4:
		rst+=1
	if rst == 6:
		return 0
	else:
		return 1
		
def function1():
	global p11
	global p12
	global p13
	global p14
	
	mid1 = p11
	p11 = p14
	p14 = p13
	p13 = p12
	p12 = mid1
	
def function2():
	global p13
	global p22
	global p23
	global p42
	
	
	mid2 = p13
	p13 = p42
	p42 = p23
	p23 = p22
	p22 = mid2
	
def function3():
	global p31
	global p14
	global p41
	global p34

	mid3 = p31
	p31 = p34
	p34 = p41
	p41 = p14
	p14 = mid3
	
def function4():
	global p41
	global p42
	global p43
	global p44
	
	mid4 = p41
	p41 = p44
	p44 = p43
	p43 = p42
	p42 = mid4
	
	
	
	#for random try-no limit  step- 至少10步不可能了
def bd_temple_code():

	global p41
	global p42
	global p43
	global p44
	target_step = 60
	hand = [0]*(target_step+2)
	
	a = 1
	sum_time = 0
	while(a):
		
		sum_total = 0
		sum_time+=1
		if sum_time%20000 == 0
			print('processing...')
			sum_time = 1
		#target = 5**20
		#sum_20 = 0
		#break_wai = 0
		#no_work = 0
		#print("target is : "+str(target))
		#print('Number is start operation from right to left')

		p11 = 3
		p12 = 2
		p13 = 3
		p14 = 4
		p22 = 3
		p23 = 2
		p31 = 2
		p34 = 3
		p41 = 4
		p42 = 4
		p43 = 4
		p44 = 2
		
		while(check()):
			

			tgt = int(random.random()*4)+1
			
			hand[sum_total]=tgt
			print(str(hand[sum_total]))
			if tgt ==1:
				function1()
			elif tgt == 2:
				function2()
			elif tgt == 3:
				function3()
			elif tgt == 4:
				function4()
			else:
				print('Error, no value large than 4!!!\n')
			#print(str(tgt)+'->', end ='')
					
		
			sum_total+=1
			
			if sum_total>target_step:
				#print("\n step over 40, no use this way.\n")
				hand = [0]*(target_step+2)
				break
		#print('\n')
		
		if sum_total <=target_step:
			print('\n finish, sum_total: '+ str(sum_total))
			with open('/result_Baldur_gate.txt', 'w') as f_w:
				for i in range(0, target_step):
					f_w.write(str(hand[i])+' -> ')
			a = 0
			break
		
		
		#print(str(sum_total))
	
'''
#for all try-20 step- 至少10步不可能了
def bd_temple_code():

	global p41
	global p42
	global p43
	global p44

	a = 1

	while(a):
		
		target = 5**20
		sum_20 = 0
		break_wai = 0
		no_work = 0
		print("target is : "+str(target))
		print('Number is start operation from right to left')

		
		hand = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		
		while(sum_20<target):
			#func = int(random.random()*4)+1
			p11 = 3
			p12 = 2
			p13 = 3
			p14 = 4
			p22 = 3
			p23 = 2
			p31 = 2
			p34 = 3
			p41 = 4
			p42 = 4
			p43 = 4
			p44 = 2
			
			if no_work !=1:
				if sum_20%100000000000 == 0:
					print(hand)
				for i in range(0,20):
					tgt = hand[19-i]
					if tgt == 0:
						pass
					elif tgt ==1:
						function1()
					elif tgt == 2:
						function2()
					elif tgt == 3:
						function3()
					elif tgt == 4:
						function4()
					else:
						print('Error, no value large than 4!!!\n')
					#print(str(func)+'->', end ='')
					
					if i == break_wai:
						break
			else:
				no_work = 0
				
			if check()==0:
				print(hand)
				break
			#进位
			
			sum_20 += 1

			sum_20_shang = int(sum_20)
			#print('sum_20 is: '+str(sum_20))
			for j in range(0, 20):
				hand[19-j]=sum_20_shang%(5)
				sum_20_shang = int(sum_20_shang/5)
				if sum_20_shang>0 and hand[19-j]==0:
					no_work = 1
					break
				if sum_20_shang == 0:
					break_wai = j

		a = 0
		
			#sum+=1
			
			#if sum>20:
				#print("\n step over 20, no use this way.\n")
				#break
		#if sum <=20:
			#print('\n finish')
			#break
'''
bd_temple_code()

import sys
# from tabulate import tabulate


tabela_lr = {
	'0': {'51': 's2', '53': 'r1', '57': 's3', '46,48': None, '4,57': 's4', '28': None, '30': None, '32': None, '34': 'r1', '9,57': None, '15,57': 's5', '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': 'r1', 'EE\'': None, 'EE': 1, 'NN': None},
	'1': {'51': None, '53': None, '57': None, '46,48': None, '4,57': None, '28': None, '30': None, '32': None, '34': None, '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': 'acc', 'EE\'': None, 'EE': None, 'NN': None},
	'2': {'51': 's2', '53': 'r1', '57': 's3', '46,48': None, '4,57': 's4', '28': None, '30': None, '32': None, '34': 'r1', '9,57': None, '15,57': 's5', '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': 'r1', 'EE\'': None, 'EE': 6, 'NN': None},
	'3': {'51': None, '53': None, '57': None, '46,48': 's7', '4,57': None, '28': None, '30': None, '32': None, '34': None, '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'4': {'51': None, '53': None, '57': None, '46,48': None, '4,57': None, '28': 's8', '30': None, '32': None, '34': None, '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'5': {'51': None, '53': None, '57': None, '46,48': None, '4,57': None, '28': 's9', '30': None, '32': None, '34': None, '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'6': {'51': None, '53': 's10', '57': None, '46,48': None, '4,57': None, '28': None, '30': None, '32': None, '34': None, '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'7': {'51': None, '53': None, '57': 's12', '46,48': None, '4,57': None, '28': 's14', '30': None, '32': None, '34': None, '9,57': None, '15,57': None, '59': 's13', '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': 's15', '$': None, 'EE\'': None, 'EE': None, 'NN': 11},
	'8': {'51': None, '53': None, '57': 's12', '46,48': None, '4,57': None, '28': 's14', '30': None, '32': None, '34': None, '9,57': None, '15,57': None, '59': 's13', '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': 's15', '$': None, 'EE\'': None, 'EE': None, 'NN': 16},
	'9': {'51': None, '53': None, '57': 's12', '46,48': None, '4,57': None, '28': 's14', '30': None, '32': None, '34': None, '9,57': None, '15,57': None, '59': 's13', '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': 's15', '$': None, 'EE\'': None, 'EE': None, 'NN': 17},
	'10': {'51': 's2', '53': 'r1', '57': 's3', '46,48': None, '4,57': 's4', '28': None, '30': None, '32': None, '34': 'r1', '9,57': None, '15,57': 's5', '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': 'r1', 'EE\'': None, 'EE': 18, 'NN': None},
	'11': {'51': None, '53': 'r3', '57': None, '46,48': None, '4,57': None, '28': None, '30': None, '32': None, '34': 'r3', '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': 'r3', 'EE\'': None, 'EE': None, 'NN': None},
	'12': {'51': 'r7', '53': 'r7', '57': None, '46,48': None, '4,57': None, '28': None, '30': 'r7', '32': None, '34': 'r7', '9,57': None, '15,57': None, '59': None, '38': 'r7', '36': 'r7', '44': 'r7', '42': 'r7', '40': 'r7', '55': 'r7', '18,57': 'r7', '22,57': 'r7', '49': 'r7', '26,57': None, '$': 'r7', 'EE\'': None, 'EE': None, 'NN': None},
	'13': {'51': 'r8', '53': 'r8', '57': None, '46,48': None, '4,57': None, '28': None, '30': 'r8', '32': None, '34': 'r8', '9,57': None, '15,57': None, '59': None, '38': 'r8', '36': 'r8', '44': 'r8', '42': 'r8', '40': 'r8', '55': 'r8', '18,57': 'r8', '22,57': 'r8', '49': 'r8', '26,57': None, '$': 'r8', 'EE\'': None, 'EE': None, 'NN': None},
	'14': {'51': None, '53': None, '57': 's12', '46,48': None, '4,57': None, '28': 's14', '30': None, '32': None, '34': None, '9,57': None, '15,57': None, '59': 's13', '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': 's15', '$': None, 'EE\'': None, 'EE': None, 'NN': 19},
	'15': {'51': None, '53': None, '57': 's12', '46,48': None, '4,57': None, '28': 's14', '30': None, '32': None, '34': None, '9,57': None, '15,57': None, '59': 's13', '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': 's15', '$': None, 'EE\'': None, 'EE': None, 'NN': 20},
	'16': {'51': None, '53': None, '57': None, '46,48': None, '4,57': None, '28': None, '30': 's21', '32': None, '34': None, '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'17': {'51': None, '53': None, '57': None, '46,48': None, '4,57': None, '28': None, '30': 's22', '32': None, '34': None, '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'18': {'51': None, '53': 'r2', '57': None, '46,48': None, '4,57': None, '28': None, '30': None, '32': None, '34': 'r2', '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': 'r2', 'EE\'': None, 'EE': None, 'NN': None},
	'19': {'51': 's33', '53': 's32', '57': None, '46,48': None, '4,57': None, '28': None, '30': None, '32': None, '34': None, '9,57': None, '15,57': None, '59': None, '38': 's23', '36': 's24', '44': 's25', '42': 's26', '40': 's27', '55': 's28', '18,57': 's29', '22,57': 's30', '49': 's31', '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'20': {'51': 'r20', '53': 'r20', '57': None, '46,48': None, '4,57': None, '28': None, '30': 'r20', '32': None, '34': 'r20', '9,57': None, '15,57': None, '59': None, '38': 'r20', '36': 'r20', '44': 'r20', '42': 'r20', '40': 'r20', '55': 'r20', '18,57': 'r20', '22,57': 'r20', '49': 'r20', '26,57': None, '$': 'r20', 'EE\'': None, 'EE': None, 'NN': None},
	'21': {'51': None, '53': None, '57': None, '46,48': None, '4,57': None, '28': None, '30': None, '32': 's34', '34': None, '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'22': {'51': None, '53': None, '57': None, '46,48': None, '4,57': None, '28': None, '30': None, '32': 's35', '34': None, '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'23': {'51': None, '53': None, '57': 's12', '46,48': None, '4,57': None, '28': 's14', '30': None, '32': None, '34': None, '9,57': None, '15,57': None, '59': 's13', '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': 's15', '$': None, 'EE\'': None, 'EE': None, 'NN': 36},
	'24': {'51': None, '53': None, '57': 's12', '46,48': None, '4,57': None, '28': 's14', '30': None, '32': None, '34': None, '9,57': None, '15,57': None, '59': 's13', '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': 's15', '$': None, 'EE\'': None, 'EE': None, 'NN': 37},
	'25': {'51': None, '53': None, '57': 's12', '46,48': None, '4,57': None, '28': 's14', '30': None, '32': None, '34': None, '9,57': None, '15,57': None, '59': 's13', '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': 's15', '$': None, 'EE\'': None, 'EE': None, 'NN': 38},
	'26': {'51': None, '53': None, '57': 's12', '46,48': None, '4,57': None, '28': 's14', '30': None, '32': None, '34': None, '9,57': None, '15,57': None, '59': 's13', '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': 's15', '$': None, 'EE\'': None, 'EE': None, 'NN': 39},
	'27': {'51': None, '53': None, '57': 's12', '46,48': None, '4,57': None, '28': 's14', '30': None, '32': None, '34': None, '9,57': None, '15,57': None, '59': 's13', '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': 's15', '$': None, 'EE\'': None, 'EE': None, 'NN': 40},
	'28': {'51': None, '53': None, '57': 's12', '46,48': None, '4,57': None, '28': 's14', '30': None, '32': None, '34': None, '9,57': None, '15,57': None, '59': 's13', '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': 's15', '$': None, 'EE\'': None, 'EE': None, 'NN': 41},
	'29': {'51': None, '53': None, '57': 's12', '46,48': None, '4,57': None, '28': 's14', '30': None, '32': None, '34': None, '9,57': None, '15,57': None, '59': 's13', '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': 's15', '$': None, 'EE\'': None, 'EE': None, 'NN': 42},
	'30': {'51': None, '53': None, '57': 's12', '46,48': None, '4,57': None, '28': 's14', '30': None, '32': None, '34': None, '9,57': None, '15,57': None, '59': 's13', '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': 's15', '$': None, 'EE\'': None, 'EE': None, 'NN': 43},
	'31': {'51': None, '53': None, '57': 's12', '46,48': None, '4,57': None, '28': 's14', '30': None, '32': None, '34': None, '9,57': None, '15,57': None, '59': 's13', '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': 's15', '$': None, 'EE\'': None, 'EE': None, 'NN': 44},
	'32': {'51': None, '53': None, '57': 's12', '46,48': None, '4,57': None, '28': 's14', '30': None, '32': None, '34': None, '9,57': None, '15,57': None, '59': 's13', '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': 's15', '$': None, 'EE\'': None, 'EE': None, 'NN': 45},
	'33': {'51': None, '53': None, '57': 's12', '46,48': None, '4,57': None, '28': 's14', '30': None, '32': None, '34': None, '9,57': None, '15,57': None, '59': 's13', '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': 's15', '$': None, 'EE\'': None, 'EE': None, 'NN': 46},
	'34': {'51': 's2', '53': 'r1', '57': 's3', '46,48': None, '4,57': 's4', '28': None, '30': None, '32': None, '34': 'r1', '9,57': None, '15,57': 's5', '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': 'r1', 'EE\'': None, 'EE': 47, 'NN': None},
	'35': {'51': 's2', '53': 'r1', '57': 's3', '46,48': None, '4,57': 's4', '28': None, '30': None, '32': None, '34': 'r1', '9,57': None, '15,57': 's5', '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': 'r1', 'EE\'': None, 'EE': 48, 'NN': None},
	'36': {'51': None, '53': None, '57': None, '46,48': None, '4,57': None, '28': None, '30': 's49', '32': None, '34': None, '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'37': {'51': None, '53': None, '57': None, '46,48': None, '4,57': None, '28': None, '30': 's50', '32': None, '34': None, '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'38': {'51': None, '53': None, '57': None, '46,48': None, '4,57': None, '28': None, '30': 's51', '32': None, '34': None, '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'39': {'51': None, '53': None, '57': None, '46,48': None, '4,57': None, '28': None, '30': 's52', '32': None, '34': None, '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'40': {'51': None, '53': None, '57': None, '46,48': None, '4,57': None, '28': None, '30': 's53', '32': None, '34': None, '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'41': {'51': None, '53': None, '57': None, '46,48': None, '4,57': None, '28': None, '30': 's54', '32': None, '34': None, '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'42': {'51': None, '53': None, '57': None, '46,48': None, '4,57': None, '28': None, '30': 's55', '32': None, '34': None, '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'43': {'51': None, '53': None, '57': None, '46,48': None, '4,57': None, '28': None, '30': 's56', '32': None, '34': None, '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'44': {'51': None, '53': None, '57': None, '46,48': None, '4,57': None, '28': None, '30': 's57', '32': None, '34': None, '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'45': {'51': None, '53': None, '57': None, '46,48': None, '4,57': None, '28': None, '30': 's58', '32': None, '34': None, '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'46': {'51': None, '53': None, '57': None, '46,48': None, '4,57': None, '28': None, '30': 's59', '32': None, '34': None, '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'47': {'51': None, '53': None, '57': None, '46,48': None, '4,57': None, '28': None, '30': None, '32': None, '34': 's60', '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'48': {'51': None, '53': None, '57': None, '46,48': None, '4,57': None, '28': None, '30': None, '32': None, '34': 's61', '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'49': {'51': 'r9', '53': 'r9', '57': None, '46,48': None, '4,57': None, '28': None, '30': 'r9', '32': None, '34': 'r9', '9,57': None, '15,57': None, '59': None, '38': 'r9', '36': 'r9', '44': 'r9', '42': 'r9', '40': 'r9', '55': 'r9', '18,57': 'r9', '22,57': 'r9', '49': 'r9', '26,57': None, '$': 'r9', 'EE\'': None, 'EE': None, 'NN': None},
	'50': {'51': 'r10', '53': 'r10', '57': None, '46,48': None, '4,57': None, '28': None, '30': 'r10', '32': None, '34': 'r10', '9,57': None, '15,57': None, '59': None, '38': 'r10', '36': 'r10', '44': 'r10', '42': 'r10', '40': 'r10', '55': 'r10', '18,57': 'r10', '22,57': 'r10', '49': 'r10', '26,57': None, '$': 'r10', 'EE\'': None, 'EE': None, 'NN': None},
	'51': {'51': 'r11', '53': 'r11', '57': None, '46,48': None, '4,57': None, '28': None, '30': 'r11', '32': None, '34': 'r11', '9,57': None, '15,57': None, '59': None, '38': 'r11', '36': 'r11', '44': 'r11', '42': 'r11', '40': 'r11', '55': 'r11', '18,57': 'r11', '22,57': 'r11', '49': 'r11', '26,57': None, '$': 'r11', 'EE\'': None, 'EE': None, 'NN': None},
	'52': {'51': 'r12', '53': 'r12', '57': None, '46,48': None, '4,57': None, '28': None, '30': 'r12', '32': None, '34': 'r12', '9,57': None, '15,57': None, '59': None, '38': 'r12', '36': 'r12', '44': 'r12', '42': 'r12', '40': 'r12', '55': 'r12', '18,57': 'r12', '22,57': 'r12', '49': 'r12', '26,57': None, '$': 'r12', 'EE\'': None, 'EE': None, 'NN': None},
	'53': {'51': 'r13', '53': 'r13', '57': None, '46,48': None, '4,57': None, '28': None, '30': 'r13', '32': None, '34': 'r13', '9,57': None, '15,57': None, '59': None, '38': 'r13', '36': 'r13', '44': 'r13', '42': 'r13', '40': 'r13', '55': 'r13', '18,57': 'r13', '22,57': 'r13', '49': 'r13', '26,57': None, '$': 'r13', 'EE\'': None, 'EE': None, 'NN': None},
	'54': {'51': 'r14', '53': 'r14', '57': None, '46,48': None, '4,57': None, '28': None, '30': 'r14', '32': None, '34': 'r14', '9,57': None, '15,57': None, '59': None, '38': 'r14', '36': 'r14', '44': 'r14', '42': 'r14', '40': 'r14', '55': 'r14', '18,57': 'r14', '22,57': 'r14', '49': 'r14', '26,57': None, '$': 'r14', 'EE\'': None, 'EE': None, 'NN': None},
	'55': {'51': 'r15', '53': 'r15', '57': None, '46,48': None, '4,57': None, '28': None, '30': 'r15', '32': None, '34': 'r15', '9,57': None, '15,57': None, '59': None, '38': 'r15', '36': 'r15', '44': 'r15', '42': 'r15', '40': 'r15', '55': 'r15', '18,57': 'r15', '22,57': 'r15', '49': 'r15', '26,57': None, '$': 'r15', 'EE\'': None, 'EE': None, 'NN': None},
	'56': {'51': 'r16', '53': 'r16', '57': None, '46,48': None, '4,57': None, '28': None, '30': 'r16', '32': None, '34': 'r16', '9,57': None, '15,57': None, '59': None, '38': 'r16', '36': 'r16', '44': 'r16', '42': 'r16', '40': 'r16', '55': 'r16', '18,57': 'r16', '22,57': 'r16', '49': 'r16', '26,57': None, '$': 'r16', 'EE\'': None, 'EE': None, 'NN': None},
	'57': {'51': 'r17', '53': 'r17', '57': None, '46,48': None, '4,57': None, '28': None, '30': 'r17', '32': None, '34': 'r17', '9,57': None, '15,57': None, '59': None, '38': 'r17', '36': 'r17', '44': 'r17', '42': 'r17', '40': 'r17', '55': 'r17', '18,57': 'r17', '22,57': 'r17', '49': 'r17', '26,57': None, '$': 'r17', 'EE\'': None, 'EE': None, 'NN': None},
	'58': {'51': 'r18', '53': 'r18', '57': None, '46,48': None, '4,57': None, '28': None, '30': 'r18', '32': None, '34': 'r18', '9,57': None, '15,57': None, '59': None, '38': 'r18', '36': 'r18', '44': 'r18', '42': 'r18', '40': 'r18', '55': 'r18', '18,57': 'r18', '22,57': 'r18', '49': 'r18', '26,57': None, '$': 'r18', 'EE\'': None, 'EE': None, 'NN': None},
	'59': {'51': 'r19', '53': 'r19', '57': None, '46,48': None, '4,57': None, '28': None, '30': 'r19', '32': None, '34': 'r19', '9,57': None, '15,57': None, '59': None, '38': 'r19', '36': 'r19', '44': 'r19', '42': 'r19', '40': 'r19', '55': 'r19', '18,57': 'r19', '22,57': 'r19', '49': 'r19', '26,57': None, '$': 'r19', 'EE\'': None, 'EE': None, 'NN': None},
	'60': {'51': None, '53': 'r4', '57': None, '46,48': None, '4,57': None, '28': None, '30': None, '32': None, '34': 'r4', '9,57': 's62', '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': 'r4', 'EE\'': None, 'EE': None, 'NN': None},
	'61': {'51': None, '53': 'r6', '57': None, '46,48': None, '4,57': None, '28': None, '30': None, '32': None, '34': 'r6', '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': 'r6', 'EE\'': None, 'EE': None, 'NN': None},
	'62': {'51': None, '53': None, '57': None, '46,48': None, '4,57': None, '28': None, '30': None, '32': 's63', '34': None, '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'63': {'51': 's2', '53': 'r1', '57': 's3', '46,48': None, '4,57': 's4', '28': None, '30': None, '32': None, '34': 'r1', '9,57': None, '15,57': 's5', '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': 'r1', 'EE\'': None, 'EE': 64, 'NN': None},
	'64': {'51': None, '53': None, '57': None, '46,48': None, '4,57': None, '28': None, '30': None, '32': None, '34': 's65', '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': None, 'EE\'': None, 'EE': None, 'NN': None},
	'65': {'51': None, '53': 'r5', '57': None, '46,48': None, '4,57': None, '28': None, '30': None, '32': None, '34': 'r5', '9,57': None, '15,57': None, '59': None, '38': None, '36': None, '44': None, '42': None, '40': None, '55': None, '18,57': None, '22,57': None, '49': None, '26,57': None, '$': 'r5', 'EE\'': None, 'EE': None, 'NN': None},
}
prod = [
	'EE\' -> EE',#EE' -> EE
	'EE -> vazio',#EE -> ''
	'EE -> 51 EE 53 EE',#EE -> < EE > EE
	'EE -> 57 46,48 NN',#EE -> 57 = NN
	'EE -> 4,57 28 NN 30 32 EE 34',#EE -> if ( NN ) { EE }
	'EE -> 4,57 28 NN 30 32 EE 34 9,57 32 EE 34',#EE -> if ( NN ) { EE } else { EE }
	'EE -> 15,57 28 NN 30 32 EE 34',#EE -> while ( NN ) { EE }
	'NN -> 57',#NN -> 57
	'NN -> 59',#NN -> 59
	'NN -> 28 NN 38 NN 30',#NN -> ( NN + NN )
	'NN -> 28 NN 36 NN 30',#NN -> ( NN - NN )
	'NN -> 28 NN 44 NN 30',#NN -> ( NN / NN )
	'NN -> 28 NN 42 NN 30',#NN -> ( NN ^ NN )
	'NN -> 28 NN 40 NN 30',#NN -> ( NN * NN )
	'NN -> 28 NN 55 NN 30',#NN -> ( NN " NN )
	'NN -> 28 NN 18,57 NN 30',#NN -> ( NN or NN )
	'NN -> 28 NN 22,57 NN 30',#NN -> ( NN and NN )
	'NN -> 28 NN 49 NN 30',#NN -> ( NN == NN )
	'NN -> 28 NN 53 NN 30',#NN -> ( NN > NN )
	'NN -> 28 NN 51 NN 30',#NN -> ( NN < NN )
	'NN -> 26,57 NN' #NN -> not NN
]

# Nonterminal FIRST               FOLLOW
# EE'         {'',<,AI,if,while}  {$}
# EE          {'',<,AI,if,while}  {$,>,}}
# NN          {AI,AH,(,not}       {$,>,),+,-,/,^,*,",or,and,==,<,}}
def visualize(pilha, fita, acao):
    print(pilha, end=' ')  # Imprime o conteúdo da pilha sem quebrar a linha
    for i in fita:
        print(i[1], end=' ')  # Imprime apenas o segundo elemento de cada item da fita (ignorando o primeiro)
    print(acao)  # Imprime a ação atual

# Inicialize uma lista vazia para 'fita'
fita = []

# Leia as linhas do arquivo 'out_lexical.txt' e adicione-as à 'fita'
with open('out_lexical.txt') as programa:
    for linha in programa:
        fita.append(linha.split())  # Divide a linha em elementos e adiciona-os à lista 'fita'

# Crie a lista de cabeçalhos da tabela
# cabecalhos = ['Estado'] + list(tabela_lr.get('$', {}).keys())


# Crie a lista de linhas da tabela
linhas = []
for estado, acoes in tabela_lr.items():
    linha = [estado] + [valor if valor else '-' for valor in acoes.values()]
    linhas.append(linha)

# Imprima a tabela no terminal
# print(tabulate(linhas, headers=cabecalhos, tablefmt='pipe'))

# Inicialize 'pilha' com o valor inicial
pilha = ['0']
acao = ''

while True:
    # Verifique se o topo da 'pilha' é numérico
    if pilha[-1].isnumeric():
        acao = tabela_lr[pilha[-1]][fita[0][1]]  # Obtém a ação correspondente na tabela_lr
        visualize(pilha, fita, acao)  # Chama a função visualize para exibir o estado atual

        # Ver

        # Verifique erros e lide com as ações adequadamente
        if not acao:  # Se não houver ação, ocorreu um erro de sintaxe
            sys.exit('erro (sintaxe inválida) linha {} token {}'.format(fita[0][0], fita[0][2]))
        elif acao[0] == 's':  # Se a ação começa com 's', empilhe o terminal e o estado
            pilha.append(fita[0][1]) #representa o empilhamento 
            fita.pop(0) # Essa instrução remove e retorna o primeiro elemento da lista fita
            pilha.append(acao[1:]) #representa o empilhamento 
        elif acao[0] == 'r':  # Se a ação começa com 'r', aplique a regra de redução
            temp = prod[int(acao[1:])].split()  # Obtém a produção correspondente na lista 'prod'
            for i in range((len(temp) - 2) * 2):  #determina o tamanho da produção e quantos símbolos devem ser desempilhados durante a aplicação da regra de redução.
                pilha.pop() # permite desempilhar um símbolo do topo da pilha de estados.
            pilha.append(temp[0]) #adiciona um novo elemento no topo da pilha
        else:
            break  # Se a ação não corresponder a 's' ou 'r', interrompe o loop
    else:
        acao = tabela_lr[pilha[-2]][pilha[-1]]  # Obtém a ação correspondente na tabela_lr
        visualize(pilha, fita, acao)  # Chama a função visualize para exibir o estado atual
        pilha.append(str(tabela_lr[pilha[-2]][pilha[-1]]))  # Empilha a ação como uma string

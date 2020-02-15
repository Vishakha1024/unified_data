from reader import vowel_counter_enhanced
import matplotlib.pyplot as plt 

def vowels_bar(file):
 results = vowel_counter_enhanced(file)
 print(results)
 x = results.keys()
 h = results.valves()
 c = ['blue','yellow']
 plt.bar(x,h,color=c)
 plt.show()


file = 'data/Richardson_Clarissa.txt'
vowels_bar(file)
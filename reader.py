def read_file(filepath):
      f = open(filepath,errors='ignore')
      data = f.read()
      f.close()
      return data
def vowel_counter(file):
    data = read_file(file).lower()
    vowels = 'aeiou'
    total_vowels = 0
    for item in vowels:
        total_vowels+=data.count(item)
    return total_vowels
def vowel_counter_enhanced(file):
     vow= {}
     data = read_file(file).lower()
     vowels = 'aeiou'
     total_vowels = 0
     for item in vowels:
         total_vowels+=data.count(item)
     return total_vowels
# calling function 1 
file = 'data/Richardson_clarissa.txt'
t_v = vowel_counter(file)
for vowels in t_v:
    print('total no. of vowels are',t_v)

   
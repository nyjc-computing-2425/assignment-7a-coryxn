# Write a function to convert numbers to text numerals

def text_numeral(n):
  """
  a greedy algorithm that converts numbers to text

  Parameters
  -----------
  n: int
    number to be converted

  Returns
  ---------
  str
    
  """
  NUM_WORD = {
    1: "one",
    2: "two",
    3: "three",
    4: "four" ,
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
  }
  
  record = []
  keyslist = list(NUM_WORD.keys())
  valueslist = list(NUM_WORD.values())
  # start: len(NUM_WORD)-1 as 27-1 = 26 and we nd values 0-26
  # end: -1 so last number wld be index 0 (ie 1:'one')
  # step: -1 reverses range
  # format is range(end, start, -step) for reversing lists
  for i in range(len(keyslist)-1, -1, -1):
    if n >= keyslist[i]:
      n -= keyslist[i]
      record.append(valueslist[i])
  print(' '.join(record))  

# text_numeral(36)
  
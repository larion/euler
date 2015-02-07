module Euler17 (numToEnglishString) where

-- count the number of characters in the first one thousand numbers written out in English
main = print $ length $ foldl1 (++) $ map (deleteChars . numToEnglishString) [1..1000]
     where deleteChars = filter (\x -> x/= ' ' &&  x /= '-')

-- convert an Integer to its English name (up to 9999)
numToEnglishString::Int -> String
numToEnglishString 0 = ""
numToEnglishString n
    | magnitude == 0               = smallNums!!mSD
    | magnitude == 1 && mSD > 1    = midNums!!mSD ++ (if rest/="" then "-" ++ rest else "")
    | magnitude == 1 && mSD <= 1   = smallNums!!n
    | magnitude == 2               = smallNums!!mSD ++ (if rest/="" then " hundred and " ++ rest else " hundred")
    | magnitude == 3               = smallNums!!mSD ++ (if rest/="" then " thousand and " ++ rest else " thousand")
    where magnitude =  floor (log10 n)
          mSD       =  n `div` (10^magnitude) -- the most significant digit
          rest      =  numToEnglishString (n-mSD*10^magnitude)

log10::Int -> Double
log10 x = roundToPrecision 9 (logBase 10 (fromIntegral x))

roundToPrecision p n = fromInteger (round $ n * (10^p)) / (10.0^^p)

-- constants
smallNums     = ["zero", "one", "two", "three", "four", "five", "six",
              "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen",
              "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
midNums       = ["zero", "teen", "twenty", "thirty", "fourty", "fifty",
              "sixty", "seventy", "eighty", "ninty"]

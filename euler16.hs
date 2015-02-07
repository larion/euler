main = print $ digitSumPowerOfTwo 1000

digitSumPowerOfTwo pow = sum $ digitsAsStrings (iterate (*2) 1 !! pow)
    where digitsAsStrings = map (read . (\c -> [c])) . show

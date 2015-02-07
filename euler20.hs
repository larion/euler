main = print $ sum $ map read fact100
       where fact100 = map (:[]) $ show $ product [1..100]

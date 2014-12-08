main = print $ maximum [(collatzLen x, x) | x <- [500001, 500003..999999]]

-- length of collatz chain from a number until it reaches 1
collatzLen :: Int -> Int
collatzLen 0 = 1
collatzLen 1 = 1
collatzLen x = collatzLen (collatzSucc x) + 1
    where collatzSucc x 
               | even x         =  x `quot` 2
               | otherwise      =  3 * x + 1

-- collatz chain associated with a number
collatzChain :: Int -> [Int]
collatzChain 1 = [1]
collatzChain x = x : collatzChain (collatzSucc x) where
    collatzSucc x 
               | even x         =  x `quot` 2
               | otherwise      = 3*x + 1

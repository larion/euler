triangle18 = [
    [75],
    [95,64],
    [17,47,82],
    [18,35,87,10],
    [20,04,82,47,65],
    [19,01,23,75,03,34],
    [88,02,77,73,07,63,67],
    [99,65,04,28,06,16,70,92],
    [41,41,26,56,83,40,80,70,33],
    [41,48,72,33,47,32,37,16,94,29],
    [53,71,44,65,25,43,91,52,97,51,14],
    [70,11,33,28,77,73,17,78,39,68,17,57],
    [91,71,52,38,17,14,91,43,58,50,27,29,48],
    [63,66,04,68,89,53,67,30,73,16,69,87,40,31],
    [04,62,98,27,23,09,70,98,73,93,38,53,60,04,23]
    ]

infinity = read("Infinity")::Double

main = maxPathInTriangle triangle18

-- Take the maximum from the path weights in the last row of a triangle
maxPathInTriangle triangle = maximum maxPathList where 
    maxPathList = [maxPath triangle lastIndex col | col <- [0..lastIndex]] where 
        lastIndex = (length triangle) - 1

-- The weight of the maximal path from the top cell to the cell at 
-- row, col.
--
-- The maximal path in the first row is simply the value of the top number
--
-- Pretend that everything out of bounds is negative infinity (so that we
-- can generalize to negative numbers). This way no path will go out of the
-- triangle.
--
-- Otherwise the weight of the maximal path is the maximum of the left
-- upper and the right upper cell + the value of the current cell

maxPath triangle row col
    | row==0                = head $ head triangle
    | col < 0 || col > row  = - infinity
    | otherwise             = max left right + triangle !! row !! col
    where
        left = maxPath triangle (row-1) (col-1)
        right = maxPath triangle (row-1) col


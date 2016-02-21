#lang racket

; Miller-Rabin primality test
;
; the main idea for fast modular exponentiation is:
; a^e mod m ---> ( a^(e/2) mod m )^2 mod m   if e is even
; a^e mod m ---> ( a^(e-1) mod m ) * (a mod m) mod m   if e is odd
; this way we just have to do Theta(log(n)) simple operations
; (i.e. multiplications with numbers smaller than m) to calculate
; the modular exponent.
;
; Also a^2 = 1 (mod p) then a is either 1 or (p-1)
; so we check that too at every squaring step
; (if it's not 1 or (p-1) then p is not a prime)
;
; Finally use this version of Fermat's Little Theorem
; m^(p-1) = 1 (mod p)

(define (expmod-with-signal a e m)
  (define (square x) (* x x))
  (define (signal-if-non-trivial-square-root x sqx)
    (if (and
          (not (or (= x 1) (= x (sub1 m))))
          (= sqx 1) )
      0
      sqx))
  (cond
    [(= e 1) (remainder a m)]
    [(even? e)
     (let* [
       (inner (expmod-with-signal a (/ e 2) m))
       (r
        (remainder
          (square inner)
          m))]
       (signal-if-non-trivial-square-root inner r))]
    [else
      (remainder
        (* a (expmod-with-signal a (sub1 e) m))
        m)]))

(define (miller-rabin-test n m)
    (let [(rem (expmod-with-signal m (sub1 n) n))]
        (= 1 rem)))

(define (is-prime? n)
    (foldr
      (lambda (x y) (and (miller-rabin-test n x) y))
      #t
      '(2 3 5 7 11 13 17))) ; enough to test these for p < 341,550,071,728,321

(define (count-primes i to count)
    (and (= (remainder i 100000) 0) (printf "~a: ~a~n" i count))
    (if (> i to)
        count
        (let [(a_n (sub1 (* 2 (expt i 2))))]
            ;(displayln a_n)
            (if (is-prime? a_n)
                (count-primes (add1 i) to (add1 count))
                (count-primes (add1 i) to count)))))

(print (+ 2 (count-primes 2  1000000 0)))

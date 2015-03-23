#lang racket

(require rackunit)

(define (daysInMonth month year)
    (cond
      [(member month '(4 6 9 11)) 30]
      [(eq? month 2) (if (leapYear? year) 29 28)]
      [else 31]))

(define (leapYear? year)
  (if (eq? (remainder year 4) 0)
    (if (eq? (remainder year 100) 0)
      (if (eq? (remainder year 400) 0)
        #t
        #f)
      #t)
    #f))

(define (daysInYear year) (if (leapYear? year) 366 365))

(define (daysSince1900 day month year)
  (+
    day
    (apply + (map (lambda (month) (daysInMonth month year)) (range 1 month)))
    (apply + (map daysInYear (range 1900 year)))))

(define (sunday? day month year)
  (= 0 (remainder
         (daysSince1900 day month year)
         7)))

(count (lambda (x) (apply sunday? 1 x))
       (for*/list ([yr (range 1901 2001)]
                   [mo (range 1 13)])
         (list yr mo)))

(check-false (leapYear? 1900))
(check-true (leapYear? 1904))
(check-true (leapYear? 2000))

(check-false (sunday? 1 1 1900))
(check-false (sunday? 1 8 1901))
(check-true (sunday? 1 9 1901))

(check-eq? 42004 (daysSince1900 1 1 2015))

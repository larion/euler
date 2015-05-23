(use srfi-1)

;; simple:
;(define (divisorsum n)
;  (apply +
;    (filter (lambda (x) (zero? (remainder n x)))
;            (iota (sub1 n) 1))))

; optimized:
(define (divisorsum n)
  (apply +
    1
    (map (lambda (x)
      (if (not (= (* x x) n))
        (+ x (/ n x))
        x))
    (filter (lambda (x) (zero? (remainder n x)))
            (iota (sub1 (floor (sqrt n))) 2)))))

(write
  (apply +
  (filter (lambda (n)
            (and
              (= (divisorsum (divisorsum n)) n)
              (not (= (divisorsum n) n))))
    (iota 9998 2))))

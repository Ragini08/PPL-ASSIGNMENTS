;LISP PROGRAM ASSIGNMENT 7
;a)
(terpri)
(princ "-----------------------------------------------------")(terpri)
;function to get nth element of list
(defun getelement(n)
	(setq n(- n 1))
	(nth n '(11 12 13 14 15 16 a b c x y z Ragini ghijk))
)
(princ "ENTER VALUE OF n : ")
(setq ele(read))
(format t "The element at ~D position is : ~D " ele (getelement ele) )
;b)
(terpri)
(princ "-----------------------------------------------------")(terpri)
(princ "ENTER A NUMBER TO CALCULATE ITS FACTORIAL : ")
(setq num(read))
(setq a 1)
;recursive function for factorial
(defun factrecursion(n)
	(if(= n 1)
		(setq a 1)
	)
	(if(> n  1)
		(setq a(* n (factrecursion(- n 1))))
	)
	
	a
	)
(terpri)
(format t "~D factorial is ~D  ---using recursion" num (factrecursion num))
(terpri)

;iterative function for factorial
(defun fact1(n) 
    (setf ft 1)
    (do ((i n (- i 1))) ((= i 1))
        (setf ft (* ft i))
    )
	ft
)

(format t "~D factorial is ~D  ---using iteration" num (fact1 num))
(terpri)
(princ "-----------------------------------------------------")(terpri)
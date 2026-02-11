(defun square (x)
  (* x x))

(print (map #'square (range 10)))

(defun adder (x)
  (lambda (y) (setq x (+ x y))))

(let ((a (adder 10)))
  (dotimes (i 5)
    (print (funcall a 3))))

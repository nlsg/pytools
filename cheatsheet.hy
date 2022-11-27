#!/usr/bin/env hy
(import os [system]
        sys [exit argv path]
        collections [namedtuple])
(.insert path 1 "/home/nls/py/lib");
(import nls_func [Effect tee])
(require hyrule [-> ->> as->])

(defn ensure [arg condition [on-fail-form 'None]]
  "calls condition fith arg, if true: return arg, if false execute on-fail-form "
  (if (condition arg) arg (hy.eval on-fail-form )))

(setx Request       (namedtuple "Request" ["lang" "query"]))
        
(defn parse-args [argv]
  (if (< (len argv) 2)  (return (Request "" "")))
  (let [[lang #* query] argv]
    (match (.split (.join "+" query) "/") 
           [query]      (return (Request lang query))
           [_ query]    (return (parse-args (.split query "+"))))))

(defn main []
  (-> (py "argv[1:]")
      parse-args
      (ensure (fn [r] (!= r.lang "")) '(do (print "USAGE")(exit)))
      ((fn [r] (+ "curl cht.sh/" r.lang "/" r.query)))
      print))

(if (= __name__ "__main__") (main))



(defn test []
  (.insert path 1  "/home/nls/py/cnav")
  (import cnav [nav])
  (setv test-set (, (, "python" "json")
                    (, "vim")
                    (, "vim" "map" "/python" "json")
                    (, "vim" "map" "/leader")
                    (, "vim" "map" "normal" "command")
                    (, "hy" "gfor")))
  (-> test-set 
      (nav {"horizontal_split" True})
      parse-args
      print))


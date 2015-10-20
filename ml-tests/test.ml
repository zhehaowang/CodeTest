(* Practice problems for OCaml *)

(* why 
   $ ocaml < something.ml gives error 
   while
   $ ocaml
     ocaml#> #use "something.ml";;
   works?
*)

(* Practice: Drop every n-th element *)

(* OCaml is left to right, for line 11
  a::temp b n (m-1) is right;
  a::temp b n m-1 becomes (a::temp b n m)-1, and is wrong
*)

let rec temp list n m = 
  match list with 
    | a :: b -> if m = 1 
                  then temp b n n 
                  else a::temp b n (m-1)
    | [] -> [];; (* Returning None here would be wrong, as None is a different type; Some (something) appears to be the same type as None *)

let drop list n = 
  temp list n n;;

let test1 = drop [1;2;3;4] 1;;
let test2 = drop [1;2;3;4] 2;;
let test3 = drop [1;2;3;4] 3;;

(* Moral:
   Think in terms of what a function takes, and what something returns; 
   Find how the idea of local variable works; 
   Think in terms of recursion; *)


(* Practice: see if the first element of array matches *)

let match_first list a =
  match list with
    | h::t -> if a = h then true else false
    | [] -> false

(* Doing | a::t -> true would be wrong, as a in the match condition is a rebound local variable, not the one we passed in the param list *)


(* 99 Problems in OCaml, https://ocaml.org/learn/tutorials/99problems.html *)

exception ListError;;

(* 1: return the last element of list *)

let rec return_last_element list = 
  match list with
    | a :: [] -> Some a
    | a :: b -> return_last_element b
    | [] -> None;;

let return_last_element_test1 = return_last_element [1;2;3;4];;
let return_last_element_test1 = return_last_element [1];;
let return_last_element_test1 = return_last_element [];;

(* Practice: return the last N elements of an array *)

(*
let return_last_n_elements list n = 
  match list with 
    | [] -> None
    | [a] -> None
    | h @ [a, b] -> [a, b];;
*)

(* 2: find the last and penultimate *)

(* My solution *)
let rec return_last_two_element list = 
  match list with
    | [] -> None
    | h :: t -> 
      (match t with 
         | a :: b -> 
            (match b with 
               | s :: [] -> Some [a; s]
               | [] -> None
               | _ -> return_last_two_element t)
         | [] -> None)

let return_last_two_element_test0 = return_last_two_element [1;2;3;4]
let return_last_two_element_test1 = return_last_two_element [1]
let return_last_two_element_test2 = return_last_two_element []

(* Given solution *)
let rec return_last_two_element_given list = 
  match list with
    | [] -> None
    | [_] -> None
    | [x; y] -> Some [x; y]
    | h :: t -> return_last_two_element_given t

let return_last_two_element_given_test0 = return_last_two_element_given [1;2;3;4]
let return_last_two_element_given_test1 = return_last_two_element_given [1]
let return_last_two_element_given_test2 = return_last_two_element_given []

(* Moral: match with is more flexible than I thought; it can be [ele1;ele2], ele1 :: list, [only_ele], etc *)

(* 3: find the k-th element in a list *)
let rec find_kth_element k list = 
  if k < 1 then 
    None 
  else (
    match list with
      | h :: t -> if (k = 1) then (Some h) else (find_kth_element (k-1) t)
      | [] -> None
  )

let find_kth_element_test0 = find_kth_element 0 [1;2;3;4]
let find_kth_element_test1 = find_kth_element 2 [1;2;3;4]
let find_kth_element_test2 = find_kth_element 4 [1;2;3;4]
let find_kth_element_test2 = find_kth_element 8 [1;2;3;4]

(* 4: find the number of elements in a list *)
let number_of_elements = 
  let rec number_of_elements_helper num helper_list = 
    match helper_list with 
      | [] -> num
      | h :: t -> number_of_elements_helper (num + 1) t
  in number_of_elements_helper 0

let number_of_elements_test0 = number_of_elements [1;2;3;4]
let number_of_elements_test1 = number_of_elements []
let number_of_elements_test2 = number_of_elements [1]

(* Moral: h::t is a tail recursive; OCaml (let x = function | X -> XX) equals with (let x param = match param with | X -> XX *)

(* 5: reverse a list *)
let reverse_list list = 
  let rec reverse_list_helper reversed_list given_list = 
    match given_list with
      | [] -> reversed_list
      | h :: t -> reverse_list_helper (h :: reversed_list) t
  in reverse_list_helper [] list

let reverse_list_test0 = reverse_list [1;2;3;4]
let reverse_list_test1 = reverse_list []
let reverse_list_test2 = reverse_list [1]


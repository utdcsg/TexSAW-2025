let l1 = [324;285;342;153;354;153;342;345;153;375];;

let l2 = [348;303;360;345;291;357;369;291;285;294];;

let l3 = [147;348;285;144;306;285;144;297;156;327];;

let e = l2 @ l3 @ l1;;

let d x = x / 3;;

let g = (List.map d e);; 

let f = List.fold_left (+) 0 g;;

Printf.printf "sum of all flag elements: %d\n" f;;

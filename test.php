<?php
// 自分の得意な言語で
// Let's チャレンジ！！
$array = [[1, 8], [2, 8, 1], [3, 8, 1, 3]];


for($i = 0; $i < $n; $i++) {
  // $input_line = explode(" ", fgets(STDIN));
  // print_r($input_line);
  # input_lineは配列が入っている
  $m = $input_line[0];
  for ($j=1; $j <= $m; $j++) {
    echo $input_line[$j]." ";
    if ($j >=1 ) {
      echo " ";
    }
  }
}


?>

<?php
// 自分の得意な言語で
// Let's チャレンジ！！
$n = fgets(STDIN);
echo($n);

for($i = 0; $i < $n; $i++) {
  $input_line = explode(" ", fgets(STDIN));
//   print_r($input_line);
  
  # input_lineは配列が入っている
  $m = $input_line[0];
  print_r($input_line);
//   echo($m);
//   for ($j=1; $j <= $m; $j++) {
//       echo($j);
//     // echo $input_line[$j];
//     // echo(' ');
//     if ($j >=1 ) {
//       echo "";
//     }
//   }
}

?>

nは3？

Array
(
    [0] => 1
    [1] => 8

)
Array
(
    [0] => 2
    [1] => 8
    [2] => 1

)
Array
(
    [0] => 3
    [1] => 8
    [2] => 1
    [3] => 3

)


$m は1,2,3

inputlineの個数分とjが同じとき

<?php
// 自分の得意な言語で
// Let's チャレンジ！！
$n = fgets(STDIN);
// echo($n);
// $j = 1;

for($i = 0; $i < $n; $i++) {
  $input_line = explode(" ", fgets(STDIN));
//   print_r($input_line);
  
  # input_lineは配列が入っている
  $m = $input_line[0];
//   print_r($input_line);
//   echo($m);
  for ($j=1; $j <= $m; $j++) {
    echo($j).' ';
    // echo $input_line[$j].' ';
    
    if ($j >=1 ) {
    //   return;
     continue;
    }
  }
}

?>


<?php
// 自分の得意な言語で
// Let's チャレンジ！！
$n = fgets(STDIN);
// $input_line = explode(" ",fgets(STDIN));

// $m = $input_line[0];
// echo($m)
// for($l=1; $l <= $m; $l++) {
//     echo($l)
//     echo(' ');
// }

for($i = 0; $i < $n; $i++){
    $input_line = explode(" ",fgets(STDIN));
    $m = $input_line[0];
    // print_r($input_line);
    // print_r($m);
    for($j=1; $j <= $m; $j++) {
        echo($j);
        echo(' ');
        // echo ($input_line[1]);
        // echo($input_line[1]);
        
        // echo($input_line[$j]);
        // echo ($input_line[$j]." ");
        // if($j >=1 ){
        // echo " ";
        // }
    }
}

?>


以下が答え
<!-- echo $j == $m ?  $input_line[$j] : $input_line[$j]." " ; -->

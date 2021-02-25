<?php
  // define variables and set to empty values
  $nameErr = $fnameErr = $lnameErr = $emailErr = $phoneErr = "";
  $fname = $lname = $email = $phone = "";

  if (!isset($_POST['fname'])){
    $fnameErr = "First name is required";
    echo $fnameErr;
  } else{
    $fname = $_POST['fname'];
    if (!preg_match("/^[a-zA-Z-']*$/",$fname)) {
      $nameErr = "Only letters are allowed";
      echo $nameErr;
    }
  }

  if (!isset($_POST['lname'])){
    $lnameErr = "Last name is required";
    echo $lnameErr;
  } else{
    $lname = $_POST['lname'];
    if (!preg_match("/^[a-zA-Z-']*$/",$lname)){
      $nameErr = "Only letters are allowed";
      echo $nameErr;
    }
  }

  if (!isset($_POST['email'])){
    $emailErr = "Email is required";
    echo $emailErr;
  } else{
    $email = $_POST['email'];
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)){
      $emailErr = "Invalid email format";
      echo $emailErr;
    }
  }

  $phoneErr = "Invalid phone number";
  $phone = $_POST['phone']; 
  if (!filter_var($phone, FILTER_SANITIZE_NUMBER_INT)){
    echo $phoneErr;
  }
  $check_phone_number = str_replace("-","",$phone);
  if (strlen($check_phone_number) < 10 || strlen($check_phone_number) > 14){
    echo $phoneErr;
  }
?>